from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def adminpageres(request):
    get_ses = request.session.get('ctrlid') or request.user.username
    if not get_ses:
        return redirect('index')
    context = {}
    return render(request, 'admin/adminpageres.html', context)
