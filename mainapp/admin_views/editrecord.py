from django.shortcuts import render, redirect
from mainapp.models import Scorevents

def editrecord(request):
    # Session-based authentication (admin only)
    session = request.session
    if not session.get('logid') or not session.get('ctrlid'):
        return redirect('/')

    if request.method == 'POST':
        event_id = request.POST.get('txteveid')
        evdes = request.POST.get('txtevedes')
        if event_id:
            # Edit existing event
            try:
                event = Scorevents.objects.get(evid=event_id)
                event.evdes = evdes
                event.save()
            except Scorevents.DoesNotExist:
                pass
            return redirect('/admin/eventlst/')
        elif evdes:
            # New event
            Scorevents.objects.create(evdes=evdes)
            return redirect('/admin/eventlst/')

    getctrl = request.GET.get('mycontrol')
    geteveid = request.GET.get('myeveid')
    getevedes = request.GET.get('mydes')
    getlevel = request.GET.get('mylevel')
    # Handle delete event (if needed)
    if getctrl == 'event' and geteveid:
        try:
            scorevent = Scorevents.objects.get(evid=geteveid)
            scorevent.delete()
        except Scorevents.DoesNotExist:
            pass
        return redirect('/admin/eventlst/')
    context = {
        'geteveid': geteveid,
        'getevedes': getevedes,
        'getctrl': getctrl,
        'getlevel': getlevel,
    }
    if getctrl == 'editjudge' or getctrl == 'editcandi':
        events = Scorevents.objects.all()
        context['events'] = events
    return render(request, 'admin/editrecord.html', context)
