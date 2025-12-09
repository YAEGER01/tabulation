from django.shortcuts import render
from django.http import HttpResponse
from mainapp.models import Event, Criteria

def resultcanlst(request):
    if not (request.session.get('ctrlid') or request.session.get('logid')):
        return HttpResponse('Not authorized', status=401)
    # Fetch all events
    events = Event.objects.all().order_by('evid')
    # For each event, fetch criteria
    event_list = []
    for event in events:
        criteria = Criteria.objects.filter(evid=event.evid)
        event_list.append({
            'evid': event.evid,
            'evdes': event.evdes,
            'criteria': criteria,
        })
    context = {
        'events': event_list,
    }
    return render(request, 'admin/resultcanlst.html', context)