from django.shortcuts import render
from django.shortcuts import render, redirect
from django.db import models
from django.http import HttpResponse
from mainapp.models import Scorevents, Scri, SCandidates, SJudge, Resnoshow, Rescri, Sinscore

def resultsumcandi(request):
    # session-based admin check
    if not (request.session.get('ctrlid') or request.session.get('logid')):
        return HttpResponse('Not authorized', status=401)
    getses = request.session.get('ctrlid') or request.user.username
    if not getses:
        return redirect('index')
    # note: querystring uses 'myevid'
    getevid = request.GET.get('myevid')
    # Determine number of results to show; prefer GET param 'mynores' else Resnoshow
    nores = None
    myn = request.GET.get('mynores')
    if myn:
        try:
            nores = int(myn)
        except Exception:
            nores = None
    if nores is None:
        try:
            nores = int(Resnoshow.objects.first().noshow)
        except Exception:
            nores = 0
    # Get event description
    event = Scorevents.objects.filter(evid=getevid).first()
    rowevdes = event.evdes if event else ''
    # Get criteria headers: Scri has an evid FK, use it directly
    criteria_headers = list(Scri.objects.filter(status='1', evid=getevid).distinct().order_by('scri'))

    # Fetch all Sinscore rows for this event and these criteria to compute per-candidate scores
    criteria_ids = [c.scri for c in criteria_headers]
    sins_qs = Sinscore.objects.filter(evid=getevid, scri_id__in=criteria_ids)
    # Build map (sconid_id, scri_id) -> float(inscore)
    score_map = {}
    for s in sins_qs:
        try:
            val = float(s.inscore) if s.inscore not in (None, '') else 0.0
        except Exception:
            val = 0.0
        # use the FK id fields for mapping
        key = (getattr(s.sconid, 'sconid', getattr(s, 'sconid_id', None)) or getattr(s, 'sconid_id', None),
               getattr(s.scri, 'scri', getattr(s, 'scri_id', None)) or getattr(s, 'scri_id', None))
        # Sum scores from multiple judges for the same candidate+criteria
        score_map[key] = score_map.get(key, 0.0) + val

    # Get candidates for the event
    candidates_qs = list(SCandidates.objects.filter(evid=getevid, canstatus='1'))
    # Build candidate data with per-criteria scores, totals and averages
    candidates_data = []
    for cand in candidates_qs:
        scores = []
        total = 0.0
        for cri in criteria_headers:
            key = (cand.sconid, cri.scri)
            sc = score_map.get(key, 0.0)
            scores.append(sc)
            total += sc
        avg = (total / len(criteria_headers)) if criteria_headers else 0.0
        candidates_data.append({
            'sconid': cand.sconid,
            'cano': cand.cano,
            'cname': cand.cname,
            'scores': scores,
            'total': total,
            'average': round(avg, 2),
        })
    # Sort by total descending and assign ranks
    candidates_data.sort(key=lambda x: (-x['total'], x['cano']))  # Sort by total desc, then by candidate number
    
    # Assign ranks (handling ties)
    current_rank = 1
    prev_score = None
    for i, candidate in enumerate(candidates_data):
        if prev_score is not None and candidate['total'] != prev_score:
            current_rank = i + 1
        candidate['rank'] = current_rank
        prev_score = candidate['total']

    # Apply nores limit after ranking
    if nores and nores > 0:
        candidates_sorted = candidates_data[:nores]
    else:
        candidates_sorted = candidates_data
        
    # Get judges
    judges = SJudge.objects.filter(evid=getevid).order_by('ejid')
    context = {
        'rowevdes': rowevdes,
        'criteria_headers': criteria_headers,
        'candidates': candidates_sorted,
        'getevid': getevid,
        'nores': nores,
        'judges': judges,
    }
    return render(request, 'admin/resultsumcandi.html', context)
