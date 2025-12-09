from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponse
from mainapp.models import SCandidates, Scorevents, SJudge, Sinscore, Scri

def resultcriteriadetails(request):
    if not (request.session.get('ctrlid') or request.session.get('logid')):
        return HttpResponse('Not authorized', status=401)
    idcri = request.GET.get('myevid')
    titlecri = request.GET.get('mydes', '')
    per = request.GET.get('myper', '')
    if not idcri:
        return HttpResponseBadRequest('Missing criteria id')

    # Find the Scri (criterion) and its event
    try:
        scri_id = int(idcri)
    except Exception:
        return HttpResponseBadRequest('Invalid criteria id')
    cri = Scri.objects.filter(scri=scri_id).first()
    event = Scorevents.objects.filter(evid=cri.evid_id).first() if cri else None
    judges = list(SJudge.objects.filter(evid=event.evid).order_by('ejid')) if event else []

    # If title/per were not provided via GET, fall back to Scri fields
    if not titlecri and cri:
        titlecri = cri.ctitle or ''
    if not per and cri:
        per = cri.cper or ''

    # Get candidates for this event and criterion
    candidates_qs = list(SCandidates.objects.filter(evid=event.evid, canstatus='1')) if event else []

    # Prefetch all Sinscore rows for this event+criteria to avoid N+1 queries
    sinscores = Sinscore.objects.filter(evid_id=event.evid, scri_id=scri_id) if event else Sinscore.objects.none()
    # Build a mapping (sconid_id, ejid_id) -> inscore (as float) or None if blank
    score_map = {}
    for s in sinscores:
        try:
            if s.inscore is None or s.inscore == '':
                val = None
            else:
                val = float(s.inscore)
        except Exception:
            val = None
        # use the FK id attributes to build stable keys
        key = (getattr(s, 'sconid_id', None), getattr(s, 'ejid_id', None))
        score_map[key] = val

    # Determine winner (highest total score)
    winner_id = None
    max_score = -1
    candidate_data = []
    for candidate in candidates_qs:
        judge_scores = []
        total_score = 0.0
        for judge in judges:
            # lookup in-memory score; key uses integer ids
            key = (candidate.sconid, judge.ejid)
            score = score_map.get(key, None)
            # treat None as missing (waiting); only add numeric scores to total
            if score is None:
                judge_scores.append(None)
            else:
                judge_scores.append(score)
                total_score += score
        candidate_data.append({
            'cano': candidate.cano,
            'cname': candidate.cname,
            'judge_scores': judge_scores,
            'total_score': total_score,
            'sconid': candidate.sconid,
        })
        if total_score > max_score:
            max_score = total_score
            winner_id = candidate.sconid
    # Sort candidates by total score descending
    candidate_data.sort(key=lambda x: (-x['total_score'], x['cano']))
    
    # Assign ranks (handling ties)
    current_rank = 1
    prev_score = None
    for i, candidate in enumerate(candidate_data):
        if prev_score is not None and candidate['total_score'] != prev_score:
            current_rank = i + 1
        candidate['rank'] = current_rank
        prev_score = candidate['total_score']
        candidate['is_winner'] = (candidate['sconid'] == winner_id)

    context = {
        'event': event,
        'titlecri': titlecri,
        'per': per,
        'judges': judges,
        'candidates': candidate_data,
        'idcri': idcri,
    }
    return render(request, 'admin/resultcriteriadetails.html', context)