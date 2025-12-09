from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from mainapp.models import Candidate, Event
from django.http import JsonResponse

@login_required
def judgecanlst(request):
    getevid = request.GET.get('myevid')
    getjid = request.GET.get('myjid')
    event = Event.objects.filter(id=getevid).first()
    candidates = Candidate.objects.filter(event_id=getevid).order_by('event_id', 'category', 'cano')
    context = {
        'event': event,
        'candidates': candidates,
        'getjid': getjid,
    }
    return render(request, 'judge/judgecanlst.html', context)

def judgecanlst_status(request):
    vcanid = request.GET.get('mycanid')
    mystatus = request.GET.get('mystatus')
    # Update candidate status logic here
    Candidate.objects.filter(id=vcanid).update(canstatus=mystatus)
    return JsonResponse({'status': 'ok'})
