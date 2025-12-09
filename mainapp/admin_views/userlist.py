from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from mainapp.models import SAdmin

@login_required
def userlist(request):
    users = SAdmin.objects.all().order_by('userlevel')
    user_data = []
    for idx, user in enumerate(users, start=1):
        nUsLev = "Administrator" if user.userlevel == 0 else "User"
        user_data.append({
            'no': idx,
            'uname': user.uname,
            'username': user.username,
            'userlevel': nUsLev,
            'userid': user.userid,
            'rawlevel': user.userlevel,
        })
    context = {
        'user_data': user_data,
    }
    return render(request, 'admin/userlist.html', context)
