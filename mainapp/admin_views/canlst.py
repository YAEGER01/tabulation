from django.shortcuts import render, redirect
from mainapp.models import Scorevents, SCandidates

def canlst(request):
    # Session-based authentication (admin only)
    session = request.session
    if not session.get('logid') or not session.get('ctrlid'):
        return redirect('/')
    # List all events and their candidates
    events = Scorevents.objects.all()
    event_candidates = []
    for event in events:
        candidates = SCandidates.objects.filter(evid=event.evid).order_by('category', 'cano')
        event_candidates.append({
            'event': event,
            'candidates': candidates,
        })
    context = {
        'event_candidates': event_candidates,
        'events': events,
    }
    return render(request, 'admin/canlst.html', context)
