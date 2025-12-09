from django.shortcuts import render, redirect
from mainapp.models import Scorevents

def eventlst(request):
    # Session-based authentication (admin only)
    session = request.session
    if not session.get('logid') or not session.get('ctrlid'):
        return redirect('/')
    events = Scorevents.objects.all()
    return render(request, 'admin/eventlst.html', {'events': events})
