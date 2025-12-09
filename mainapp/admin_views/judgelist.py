from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseForbidden
from mainapp.models import Scorevents, SJudge
import hashlib


def judgelist(request):
    # Session-based authentication (admin only)
    session = request.session
    if not session.get('logid') or not session.get('ctrlid'):
        return redirect('/')

    if request.method == 'POST':
        # Handle judge creation
        judname = request.POST.get('txtname')
        juduname = request.POST.get('txtuname')
        judeve = request.POST.get('optevent')
        password = request.POST.get('txtpassword', '').strip()

        try:
            event = Scorevents.objects.get(evid=judeve) if judeve else None
        except Scorevents.DoesNotExist:
            event = None

        # Set default password if none provided
        if not password:
            password = 'password'
        md5pass = hashlib.md5(password.encode()).hexdigest()

        # Create SJudge record
        SJudge.objects.create(
            evid=event,
            jname=judname,
            uname=juduname,
            spassword=md5pass.encode()
        )

        return redirect('judgelist')

    # GET: show judge list
    events = Scorevents.objects.all()
    event_judges = []
    for event in events:
        judges = SJudge.objects.filter(evid=event)
        event_judges.append({
            'event': event,
            'judges': judges,
        })

    context = {
        'event_judges': event_judges,
        'events': events,
    }
    return render(request, 'judge/judgelist.html', context)
