from django.shortcuts import render, redirect
from mainapp.models import SAdmin

def adminpage(request):
    # Get session/controller id
    get_ses = request.session.get('ctrlid') or request.user.username
    if not get_ses:
        return redirect('index')
    # Get user info
    try:
        user = SAdmin.objects.get(userid=get_ses)
        rowuser = user.userlevel
    except SAdmin.DoesNotExist:
        rowuser = None
    context = {
        'rowuser': rowuser,
    }
    return render(request, 'admin/adminpage.html', context)
