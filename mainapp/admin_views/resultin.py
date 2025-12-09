from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse
from mainapp.models import SCandidates

def resultin(request):
    # legacy admin sessions in this project use session keys like 'ctrlid' or 'logid'
    if not (request.session.get('ctrlid') or request.session.get('logid')):
        # Return a small unauthorized response instead of redirecting to Django's login
        return HttpResponse('Not authorized', status=401)

    getevid = request.GET.get('myeveid')
    if not getevid:
        return HttpResponseBadRequest('Missing event id')

    # Get candidates for this event (SCandidates uses canstatus as a char field)
    candidates = SCandidates.objects.filter(evid=getevid, canstatus='1')
    cntcan = candidates.count()
    candidate_range = range(1, cntcan+1)

    context = {
        'getevid': getevid,
        'candidate_range': candidate_range,
        'candidates': candidates,
    }
    return render(request, 'admin/resultin.html', context)