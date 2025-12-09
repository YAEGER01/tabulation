from django.shortcuts import redirect
from mainapp.models import SCandidates

def deleteaspirant(request, sconid):
    try:
        SCandidates.objects.filter(sconid=sconid).delete()
    except Exception:
        pass
    return redirect('/admin/canlst/')