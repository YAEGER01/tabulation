from django.shortcuts import render, redirect
from mainapp.models import Scorevents, Scri

def crilst(request):
    # Session-based authentication (admin only)
    session = request.session
    if not session.get('logid') or not session.get('ctrlid'):
        return redirect('/')
    
    events = Scorevents.objects.all()
    event_criteria = []
    for event in events:
        criteria = Scri.objects.filter(evid=event.evid).order_by('scri')
        event_criteria.append({
            'event': event,
            'criteria': criteria,
        })

    # Build event dropdown: show all Scorevents (always populate dropdown)
    event_dropdown = [(s.evid, s.evdes) for s in Scorevents.objects.all()]
    # Get all events for dropdown
    event_dropdown = [(e.evid, e.evdes) for e in events]
    context = {
        'event_criteria': event_criteria,
        'events': events,
        'event_dropdown': event_dropdown,
    }
    return render(request, 'admin/crilst.html', context)
