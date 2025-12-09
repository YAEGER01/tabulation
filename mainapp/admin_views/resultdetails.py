from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponse
from mainapp.models import Scorevents, SCandidates, SJudge, Sinscore
from collections import defaultdict


def resultdetails(request):
    if not (request.session.get('ctrlid') or request.session.get('logid')):
        return HttpResponse('Not authorized', status=401)
    getevid = request.GET.get('myevid')
    nores = request.GET.get('mynores')
    try:
        nores = int(nores)
    except (TypeError, ValueError):
        nores = 10
    if not getevid:
        return HttpResponseBadRequest('Missing event id')

    event = get_object_or_404(Scorevents, pk=getevid)

    # Candidates for the event with active status
    candidates_qs = SCandidates.objects.filter(evid=getevid, canstatus='1')

    # Judges for this event (preserve order)
    judges = list(SJudge.objects.filter(evid=getevid).order_by('ejid'))
    judges_count = len(judges)

    # Prefetch all Sinscore rows for the event and build a map keyed by (sconid_id, ejid_id)
    sins = Sinscore.objects.filter(evid=getevid)
    score_map = {}
    submitted_map = defaultdict(int)
    for s in sins:
        try:
            val = float(s.inscore) if s.inscore not in (None, '') else None
        except Exception:
            val = None
        key = (getattr(s, 'sconid_id', None), getattr(s, 'ejid_id', None))
        score_map[key] = val
        if val is not None and getattr(s, 'sconid_id', None) is not None:
            submitted_map[getattr(s, 'sconid_id', None)] += 1

    # Build candidate list with per-judge scores, total and average
    candidate_list = []
    for candidate in candidates_qs:
        total = 0.0
        judge_scores = []
        for judge in judges:
            key = (candidate.sconid, judge.ejid)
            val = score_map.get(key, None)
            judge_scores.append(val)
            if val is not None:
                total += val
        average = (total / judges_count) if judges_count else 0
        candidate_list.append({
            'sconid': candidate.sconid,
            'cano': candidate.cano,
            'cname': candidate.cname,
            'grade_score': round(average, 2),
            'total_score': round(total, 2),
            'submitted_count': submitted_map.get(candidate.sconid, 0),
            'judge_scores': judge_scores,
        })

    # Sort by grade_score descending and limit
    candidate_list = sorted(candidate_list, key=lambda x: x['grade_score'], reverse=True)[:nores]

    context = {
        'event': event,
        'candidates': candidate_list,
        'judges': judges,
    }
    return render(request, 'admin/resultdetails.html', context)