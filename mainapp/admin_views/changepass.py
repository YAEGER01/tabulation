from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from mainapp.models import Gradminpas

@login_required
def changepass(request):
    user = request.user
    bmain = user.username
    # Fetch user record
    try:
        gradmin = Gradminpas.objects.get(username=bmain)
    except Gradminpas.DoesNotExist:
        gradmin = None
    msgoldpass = msgnewpass = msgconpass = message = ''
    if request.method == 'POST':
        varoldpass = request.POST.get('password', '').strip()
        varcurpass = request.POST.get('password1', '').strip()
        varconcurpass = request.POST.get('password2', '').strip()
        if not varoldpass:
            msgoldpass = 'Old Password Required'
        if not varcurpass:
            msgnewpass = 'New Password Required'
        if not varconcurpass:
            msgconpass = 'Confirm Password Required'
        if gradmin and varoldpass and varcurpass and varconcurpass:
            if check_password(varoldpass, gradmin.spassword):
                if varcurpass == varconcurpass:
                    gradmin.spassword = make_password(varcurpass)
                    gradmin.save()
                    return render(request, 'admin/changepass.html', {'success': True})
                else:
                    msgnewpass = 'Password type mis-match'
            else:
                message = 'Old Password not match Please try again'
    context = {
        'msgoldpass': msgoldpass,
        'msgnewpass': msgnewpass,
        'msgconpass': msgconpass,
        'message': message,
    }
    return render(request, 'admin/changepass.html', context)
