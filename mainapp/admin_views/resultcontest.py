from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponse
from mainapp.models import Candidate, Event, Judge, Score, Approval, Criteria

def resultcontest(request):
    if not (request.session.get('ctrlid') or request.session.get('logid')):
        return HttpResponse('Not authorized', status=401)
    getevid = request.GET.get('myevid')
    getnores = request.GET.get('mynores')
    try:
        getnores = int(getnores)
    except (TypeError, ValueError):
        getnores = 10
    if not getevid:
        return HttpResponseBadRequest('Missing event id')

    event = get_object_or_404(Event, pk=getevid)
    rowevdes = event.evdes
    judges = Judge.objects.filter(evid=getevid)

    # Calculate total percentage for event
    criteria = Criteria.objects.filter(evid=event.evid, status=1)
    disper = sum([c.cper for c in criteria])

    # Get candidates ordered by total score
    candidates_qs = Candidate.objects.filter(evid=getevid, canstatus=1)
    candidate_data = []
    max_score = -1
    winner_id = None
    for candidate in candidates_qs:
        judge_scores = []
        total_score = 0
        for judge in judges:
            score_obj = Score.objects.filter(candidate=candidate, judge=judge).first()
            score = score_obj.value if score_obj else 0
            judge_scores.append(score)
            total_score += score
        # Calculate grade_score (replace with actual logic as needed)
        judges_count = judges.count()
        restotscoreave = total_score / judges_count if judges_count else 0
        grade_score = ((restotscoreave / disper) * 50) + 50 if disper else 0
        candidate_data.append({
            'cano': candidate.cano,
            'judge_scores': judge_scores,
            'total_score': total_score,
            'grade_score': round(grade_score, 2),
            'is_winner': False,
        })
        if total_score > max_score:
            max_score = total_score
            winner_id = candidate.cano
    # Mark winner
    for c in candidate_data:
        if c['cano'] == winner_id:
            c['is_winner'] = True

    # Approvals (replace with actual logic as needed)
    approvals = []
    for judge in judges:
        # Example: get approval status for judge
        approval_obj = Approval.objects.filter(evid=getevid, ejid=judge.ejid).first()
        if approval_obj:
            status = 'Approved' if approval_obj.aprem == 'y' else 'waiting...'
            visible = 'hidden' if approval_obj.aprem == 'y' else 'visible'
        else:
            status = 'waiting...'
            visible = 'visible'
        approvals.append({'status': status, 'visible': visible})

    context = {
        'rowevdes': rowevdes,
        'getevid': getevid,
        'getnores': getnores,
        'judges': judges,
        'candidates': candidate_data,
        'approvals': approvals,
    }
    return render(request, 'admin/resultcontest.html', context)