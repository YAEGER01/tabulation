from django.http import JsonResponse
from django.views.decorators.http import require_POST
from mainapp.models import SCandidates


def toggle_candidate_status(request):
    # Simple endpoint used by admin candidates list to toggle canstatus
    # Accepts POST: sconid, status ('1' or '0')
    if request.method != 'POST':
        return JsonResponse({'ok': False, 'error': 'POST required'}, status=400)

    # session-based admin check similar to canlst
    session = request.session
    if not session.get('logid') or not session.get('ctrlid'):
        return JsonResponse({'ok': False, 'error': 'login required'}, status=403)

    sconid = request.POST.get('sconid')
    status = request.POST.get('status')
    if not sconid:
        return JsonResponse({'ok': False, 'error': 'missing sconid'}, status=400)
    if status not in ('0', '1'):
        return JsonResponse({'ok': False, 'error': 'invalid status'}, status=400)

    updated = SCandidates.objects.filter(sconid=sconid).update(canstatus=status)
    if updated:
        return JsonResponse({'ok': True, 'sconid': sconid, 'status': status})
    else:
        return JsonResponse({'ok': False, 'error': 'not found'}, status=404)


def candidate_count(request):
    # Return number of active candidates (canstatus='1') for a given event
    ev = request.GET.get('evid')
    if not ev:
        return JsonResponse({'ok': False, 'error': 'missing evid'}, status=400)
    try:
        cnt = SCandidates.objects.filter(evid=ev, canstatus='1').count()
    except Exception:
        return JsonResponse({'ok': False, 'error': 'invalid evid'}, status=400)
    return JsonResponse({'ok': True, 'evid': ev, 'count': cnt})
