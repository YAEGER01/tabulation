from django.shortcuts import redirect
from django.contrib import messages
from django.views.decorators.http import require_GET
from mainapp.models import Gradinsname
from django.db.models import Q

@require_GET
def resetpass(request):
    vargetid = request.GET.get('id')
    if vargetid:
        Gradinsname.objects.filter(id=vargetid).update(spassword='isu')  # Replace with proper password hashing
        messages.success(request, 'Password was successfully reset')
    return redirect(request.META.get('HTTP_REFERER', '/'))
