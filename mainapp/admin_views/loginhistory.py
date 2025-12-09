from django.views.decorators.http import require_POST
from django.http import JsonResponse
from mainapp.models import EsLogUser
from django.utils import timezone

@require_POST
def loginhistory(request):
    vargetusername = getattr(request, 'user', None)
    vargetdate = timezone.now()
    vargetinfo = request.POST.get('myinfo', '')
    vargetcomip = request.POST.get('mycomip', '')
    EsLogUser.objects.create(
        logdate=vargetdate,
        logusername=str(vargetusername),
        loginfo=vargetinfo,
        logcomnameip=vargetcomip
    )
    return JsonResponse({'status': 'ok'})
