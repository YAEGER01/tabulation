from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponse
from mainapp.models import Candidate, Event, Judge, Score, Criteria

def resultcandiindi(request):
    if not (request.session.get('ctrlid') or request.session.get('logid')):
        return HttpResponse('Not authorized', status=401)
    getidcri = request.GET.get('mycrid')
    getcanid = request.GET.get('mycanid')
    if not getidcri or not getcanid:
        return HttpResponseBadRequest('Missing criteria or candidate id')

    # Get event, criteria, and candidate info
    event = Event.objects.filter(scri=getidcri).first()
    titlecri = ''
    per = ''
    rowcano = ''
    if event:
        cri = Criteria.objects.filter(scri=getidcri).first()
        titlecri = cri.ctitle if cri else ''
        per = cri.cper if cri else ''
        candidate = Candidate.objects.filter(evid=event.evid, sconid=getcanid).first()
        rowcano = candidate.cano if candidate else ''
    else:
        candidate = None

    # Judges and scores
    judges = []
    total_score = 0
    if event and candidate:
        judge_qs = Judge.objects.filter(evid=event.evid).order_by('ejid')
        for judge in judge_qs:
            # Only include judges assigned to this criteria
            # (Assume a JudgeCriteria model or similar, or skip this filter if not available)
            # For now, include all judges for the event
            score_obj = Score.objects.filter(candidate=candidate, judge=judge, criteria_id=getidcri).first()
            score = score_obj.value if score_obj else 0
            judges.append({
                'ejid': judge.ejid,
                'score': score,
                'canejid': getattr(candidate, 'ejid', None),
            })
            total_score += score

    context = {
        'event': event,
        'titlecri': titlecri,
        'per': per,
        'rowcano': rowcano,
        'candidates': [candidate] if candidate else [],
        'judges': judges,
        'total_score': total_score,
    }
    return render(request, 'admin/resultcandiindi.html', context)