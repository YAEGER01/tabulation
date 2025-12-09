from django.http import JsonResponse
from django.views.decorators.http import require_POST
from mainapp.models import Scri


@require_POST
def togglecriteria(request):
    """AJAX endpoint to toggle or set Scri.status and/or Scri.category.

    POST params:
      - scri: required, Scri.pk
      - status: optional, '0' or '1' (if present set Scri.status)
      - category: optional, '0' or '1' (if present set Scri.category)

    If neither status nor category provided, the endpoint toggles status (legacy behavior).
    Only staff users are allowed to modify criteria.
    """
    # session-based admin check (matches other admin endpoints)
    session = request.session
    if not session.get('logid') or not session.get('ctrlid'):
        return JsonResponse({'ok': False, 'error': 'login required'}, status=403)

    scri_id = request.POST.get('scri')
    if not scri_id:
        return JsonResponse({'ok': False, 'error': 'missing scri id'}, status=400)
    try:
        scri = Scri.objects.get(pk=scri_id)
    except Scri.DoesNotExist:
        return JsonResponse({'ok': False, 'error': 'scri not found'}, status=404)

    status = request.POST.get('status')
    category = request.POST.get('category')
    changed = []

    if status in ('0', '1'):
        if scri.status != status:
            scri.status = status
            changed.append('status')

    if category in ('0', '1'):
        if scri.category != category:
            scri.category = category
            changed.append('category')

        # If category is being enabled for Judges Page, ensure criterion is active
        if category == '1' and (scri.status is None or scri.status != '1'):
            scri.status = '1'
            if 'status' not in changed:
                changed.append('status')

    # If no explicit param provided, toggle status (compatibility)
    if not changed and status is None and category is None:
        scri.status = '0' if scri.status == '1' else '1'
        changed.append('status')

    if changed:
        scri.save(update_fields=changed)

    return JsonResponse({'ok': True, 'scri': scri.pk, 'status': scri.status, 'category': scri.category})
