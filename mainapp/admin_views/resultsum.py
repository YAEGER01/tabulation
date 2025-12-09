from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse
from mainapp.models import SCandidates as Candidate, Scri as Criteria, Sinscore as Sinscore, Scorevents as Event

def resultsum(request):
    if not (request.session.get('ctrlid') or request.session.get('logid')):
        return HttpResponse('Not authorized', status=401)
    # Get event id from GET
    getevid = request.GET.get('myevid')
    if not getevid:
        return HttpResponseBadRequest('Missing event id')

    # Get number of results to show
    nores = request.GET.get('mynores')
    try:
        nores = int(nores)
    except (TypeError, ValueError):
        nores = 10  # default

    # Get event description
    try:
        event = Event.objects.get(pk=getevid)
        rowevdes = event.evdes
    except Event.DoesNotExist:
        rowevdes = ''

    # Get criteria headers for this event
    criteria_headers = Criteria.objects.filter(evid=getevid, status=1).order_by('pk')

    # Get candidates and their total scores
    candidates_qs = list(Candidate.objects.filter(evid=getevid))
    # Prefetch sinscore rows for event and criteria
    cri_ids = [c.scri for c in criteria_headers]
    sins = Sinscore.objects.filter(evid=getevid, scri_id__in=cri_ids)
    score_map = {}
    for s in sins:
        key = (getattr(s, 'sconid_id', None), getattr(s, 'scri_id', None))
        try:
            val = float(s.inscore) if s.inscore not in (None, '') else 0.0
        except Exception:
            val = 0.0
        # Sum scores from multiple judges for the same candidate+criteria
        score_map[key] = score_map.get(key, 0.0) + val

    candidates = []
    for candidate in candidates_qs:
        scores = []
        total = 0.0
        for cri in criteria_headers:
            key = (candidate.sconid, cri.scri)
            s_val = score_map.get(key, None)
            try:
                if s_val not in (None, ''):
                    sc = float(s_val)
                else:
                    sc = None
            except Exception:
                sc = None
            scores.append(sc if sc is not None else 0)
            if sc is not None:
                total += sc
        candidates.append({
            'candidate': candidate,
            'scores': scores,
            'total': total,
        })
    
    # Sort candidates by total score descending
    candidates.sort(key=lambda x: (-x['total'], x['candidate'].cano))
    
    # Assign ranks (1-based, handling ties)
    current_rank = 1
    prev_score = None
    for i, candidate in enumerate(candidates):
        if prev_score is not None and candidate['total'] != prev_score:
            current_rank = i + 1
        candidate['rank'] = current_rank
        prev_score = candidate['total']
    
    # Apply limit after ranking
    candidates = candidates[:nores]

    context = {
        'rowevdes': rowevdes,
        'criteria_headers': criteria_headers,
        'candidates': candidates,
        'getevid': getevid,
        'nores': nores,
    }
    return render(request, 'admin/resultsum.html', context)