from django.shortcuts import render, redirect
from mainapp.models import Scorevents, Scri


def resultcrilst(request):
    # Session-based authentication (admin)
    if not request.session.get('ctrlid'):
        return redirect('index')

    # Fetch all score events
    events = Scorevents.objects.all().order_by('evid')
    event_list = []
    for event in events:
        # Fetch criteria (Scri) for this event. Include active ones; if you want
        # all, remove the status filter.
        criteria = Scri.objects.filter(evid=event).order_by('scri')
        event_list.append({
            'evid': event.evid,
            'evdes': event.evdes,
            'criteria': criteria,
        })

    context = {'events': event_list}
    return render(request, 'admin/resultcrilst.html', context)