from django.shortcuts import render
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from dbase.models import Criteria, Event, Judge, JudgeCriteria

@login_required
def judge_criteria_list(request):
    evid = request.GET.get('myevid')
    jid = request.GET.get('myjid')
    try:
        event = Event.objects.get(pk=evid)
        judge = Judge.objects.get(pk=jid)
    except (Event.DoesNotExist, Judge.DoesNotExist):
        return HttpResponseForbidden()
    criteria = Criteria.objects.filter(evid=event)
    judge_criteria_ids = set(JudgeCriteria.objects.filter(ejid=judge).values_list('scri_id', flat=True))
    table_data = []
    for idx, cri in enumerate(criteria, 1):
        checked = cri.pk in judge_criteria_ids
        table_data.append({
            'no': idx,
            'id': cri.pk,
            'title': cri.ctitle,
            'cper': cri.cper,
            'status': cri.status,
            'checked': checked,
        })
    context = {
        'event': event,
        'judge': judge,
        'table_data': table_data,
    }
    return render(request, 'judge/judgecrilst.html', context)
