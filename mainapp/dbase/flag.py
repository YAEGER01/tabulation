import socket
import os
from datetime import datetime
from django.utils import timezone

def get_flag_context(request):
    context = {}
    if request.user.is_authenticated:
        context['myusername'] = getattr(request.user, 'username', '')
        context['mylogname'] = getattr(request.user, 'password', '')  # Not recommended to expose
        context['myctrlid'] = getattr(request.user, 'id', None)
    else:
        context['myusername'] = ''
        context['mylogname'] = ''
        context['myctrlid'] = None
    context['mydate'] = timezone.now().strftime('%m/%d/%Y')
    context['mytime'] = timezone.now().strftime('%A %d %B %Y %I:%M:%S %p')
    context['mypcname'] = socket.gethostname()
    # IP address (server-side)
    context['myip'] = request.META.get('REMOTE_ADDR', '')
    return context
