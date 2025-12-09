from django.shortcuts import render, redirect
from django.db.models import Sum
from mainapp.models import SCandidates, Scorevents, SJudge, Sinscore, Scri, Judgesapproved
from django.http import JsonResponse, HttpResponse

def result(request):
    if not (request.session.get('ctrlid') or request.session.get('logid')):
        return HttpResponse('Not authorized', status=401)
    getevid = request.GET.get('myevid')
    if not getevid:
        return redirect('adminpage')

    # Use current models: Scorevents, SCandidates, SJudge, Sinscore, Scri
    judges = list(SJudge.objects.filter(evid=getevid).order_by('ejid'))

    # Get event info
    event = Scorevents.objects.filter(evid=getevid).first()
    rowevdes = event.evdes if event else ''
    # Get number of winners
    nores = 1
    try:
        nores = int(request.GET.get('mynores', 1))
    except Exception:
        pass
    # Get criteria percent total
    qrycriteria = Scri.objects.filter(evid=getevid)
    qrypertot = qrycriteria.aggregate(totper=Sum('cper'))['totper'] or 0

    # Prefetch Sinscore rows for event and build a score map keyed by (sconid_id, ejid_id)
    candidates_qs = list(SCandidates.objects.filter(evid=getevid, canstatus='1'))
    sins = Sinscore.objects.filter(evid=getevid)
    score_map = {}
    for s in sins:
        key = (getattr(s, 'sconid_id', None), getattr(s, 'ejid_id', None))
        try:
            val = float(s.inscore) if s.inscore not in (None, '') else None
        except Exception:
            val = None
        score_map[key] = val

    candidate_totals = []
    for cand in candidates_qs:
        tot = 0.0
        for (c_id, j_id), v in score_map.items():
            if c_id == cand.sconid and v is not None:
                tot += v
        candidate_totals.append({'candidate': cand, 'tot': tot})
    sorted_candidates = sorted(candidate_totals, key=lambda x: x['tot'], reverse=True)
    top_candidates = [x['candidate'] for x in sorted_candidates[:nores]]
    winid = top_candidates[0].sconid if top_candidates else None
    # For each candidate, get judge scores and ranks
    candidate_rows = []
    for candidate in top_candidates:
        row = {'candidate': candidate, 'scores': [], 'restotscore': 0, 'is_winner': winid == candidate.sconid}
        totcrican = 0
        cntjude = 0
        totscore = 0
        totrank = 0
        gjgrade = 0
        for judge in judges:
            # Lookup score from pre-fetched map
            key = (candidate.sconid, judge.ejid)
            val = score_map.get(key, None)
            # If no numeric score, mark as waiting (None)
            if val is None:
                row['scores'].append({'rank': None, 'judge': judge})
            else:
                row['scores'].append({'rank': val, 'judge': judge})
                totscore += val
            cntjude += 1
            # totrank/gjgrade logic preserved but simplified
            totrank += (val or 0)
            gjgrade += (val or 0)
            restotscore = round(totrank / cntjude, 2) if cntjude else 0
        row['restotscore'] = restotscore
        candidate_rows.append(row)
    # Judges approval
    approvals = Judgesapproved.objects.filter(evid=getevid)
    approval_status = []
    for approval in approvals:
        appj = 'Approved' if approval.aprem == 'y' else 'waiting...'
        approval_status.append({'status': appj, 'is_waiting': approval.aprem == 'n'})
    context = {
        'getevid': getevid,
        'rowevdes': rowevdes,
        'nores': nores,
        'candidate_rows': candidate_rows,
        'judges': judges,
        'approval_status': approval_status,
        'cntapp': len(approval_status),
    }
    return render(request, 'admin/result.html', context)

def requestapproved(request):
    getevid = request.GET.get('myevid')
    nores = request.GET.get('mynores')
    # Simulate approval request logic
    Judgesapproved.objects.filter(evid=getevid).update(aprem='y')
    return JsonResponse({'message': 'Request was successfully sent'})

def cancelapproved(request):
    getevid = request.GET.get('myevid')
    Judgesapproved.objects.filter(evid=getevid).update(aprem='n')
    return JsonResponse({'message': 'Approval cancelled'})
