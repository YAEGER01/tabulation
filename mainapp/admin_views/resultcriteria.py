from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponseForbidden
from mainapp.models import Scri, Scorevents, SJudge, SCandidates, Sinscore

def resultcriteria(request):
    # Legacy session-based admin check (do not redirect to Django auth login)
    if not request.session.get('ctrlid'):
        return HttpResponseForbidden('login required')
    # idcri is the Scri primary key (criteria id)
    idcri = request.GET.get('myeveid')
    titlecri = request.GET.get('mydes', '')
    per = request.GET.get('myper', '')
    if not idcri:
        return HttpResponseBadRequest('Missing criteria id')

    # Find the Scri (criterion) and its event
    try:
        scri_id = int(idcri)
    except Exception:
        return HttpResponseBadRequest('Invalid criteria id')
    scri = Scri.objects.filter(scri=scri_id).first()
    if not scri:
        return HttpResponseBadRequest('Criterion not found')

    event = scri.evid  # Scorevents instance
    # If title/per were not provided via GET, fall back to Scri values
    if not titlecri:
        titlecri = scri.ctitle or ''
    if not per:
        per = scri.cper or ''

    # Judges assigned to this event
    judges = list(SJudge.objects.filter(evid=event).order_by('ejid')) if event else []

    # Candidates for this event (only active ones)
    candidates_qs = list(SCandidates.objects.filter(evid=event, canstatus='1').order_by('cano')) if event else []

    # Prefetch sinscore rows for this event and criterion
    sins = Sinscore.objects.filter(evid_id=event.evid, scri_id=scri_id) if event else Sinscore.objects.none()
    score_map = {}
    for s in sins:
        key = (getattr(s, 'sconid_id', None), getattr(s, 'ejid_id', None))
        try:
            if s.inscore is None or s.inscore == '':
                val = None
            else:
                val = float(s.inscore)
        except Exception:
            val = None
        score_map[key] = val

    # Compute scores per candidate per judge
    winner_id = None
    max_score = -1
    candidate_data = []
    for candidate in candidates_qs:
        judge_scores = []
        total_score = 0.0
        for judge in judges:
            key = (candidate.sconid, judge.ejid)
            score = score_map.get(key, None)
            judge_scores.append(score)
            if score is not None:
                total_score += score
        candidate_data.append({
            'judge_scores': judge_scores,
            'total_score': total_score,
            'sconid': candidate.sconid,
        })
        if total_score > max_score:
            max_score = total_score
            winner_id = candidate.sconid

    for c in candidate_data:
        c['is_winner'] = (c['sconid'] == winner_id)

    context = {
        'event': event,
        'titlecri': titlecri,
        'per': per,
        'judges': list(judges),
        'candidates': candidate_data,
        'idcri': idcri,
    }
    return render(request, 'admin/resultcriteria.html', context)