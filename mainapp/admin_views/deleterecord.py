from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from mainapp.models import (
    Scorevents,
    SJudge,
    Sinscore,
    SCandidates,
    Scri,
    SAdmin,
    Judgesapproved,
    Resall,
    Rescri,
)


@require_http_methods(['GET', 'POST'])
def deleterecord(request):
    """Generic deletion endpoint used by admin UI.

    Notes:
    - Criteria in our schema uses the `Scri` model with primary key `scri`.
    - Some older code referenced a `Criteria` model with `id` PK; support the current schema here.
    """
    # Support both GET (legacy) and POST (safer) parameters
    if request.method == 'POST':
        ctrl = request.POST.get('mycontrol')
        eveid = request.POST.get('myeveid')
    else:
        ctrl = request.GET.get('mycontrol')
        eveid = request.GET.get('myeveid')
    # Deleting an event is destructive (it will remove judges, candidates, scores, etc.).
    # Require an explicit POST with confirm=yes to proceed.
    if ctrl == 'event' and eveid:
        # accept either 'myeveid' or legacy 'myevid'
        ev_id = eveid or request.POST.get('myevid') or request.GET.get('myevid')
        if request.method != 'POST' or (request.POST.get('confirm') or request.GET.get('confirm')) != 'yes':
            return JsonResponse({
                'status': 'confirm',
                'message': 'Deleting an event will remove related judges, candidates, and scores. Resend as POST with confirm=yes to proceed.'
            })
        # Proceed with delete using current models
        try:
            # Delete all related records first
            # Delete scores and results
            Sinscore.objects.filter(evid=ev_id).delete()
            Resall.objects.filter(evid=ev_id).delete()
            Rescri.objects.filter(evid=ev_id).delete()
            
            # Delete candidates
            SCandidates.objects.filter(evid=ev_id).delete()
            
            # Delete criteria
            Scri.objects.filter(evid=ev_id).delete()
            
            # Delete judges and their approvals
            judge_ids = SJudge.objects.filter(evid=ev_id).values_list('ejid', flat=True)
            Judgesapproved.objects.filter(ejid__in=list(judge_ids)).delete()
            SJudge.objects.filter(evid=ev_id).delete()
            
            # Finally delete the event itself
            Scorevents.objects.filter(evid=ev_id).delete()
        except Exception as e:
            # If something unexpected happens, return an error status
            return JsonResponse({
                'status': 'error',
                'message': f'Failed to delete event and related records: {str(e)}'
            }, status=500)
    elif ctrl == 'judge' and eveid:
        # Require POST for delete actions for safety
        if request.method != 'POST':
            return JsonResponse({'status': 'confirm', 'message': 'Send POST to delete judge.'})
        SJudge.objects.filter(ejid=eveid).delete()
        Sinscore.objects.filter(ejid=eveid).delete()
    elif ctrl == 'judgerespass' and eveid:
        # Update judge password placeholder; actual system should hash passwords
        SJudge.objects.filter(ejid=eveid).update(spassword='isu')  # Replace with proper password hashing
    elif ctrl == 'criteria' and eveid:
        # Delete criterion using Scri.scri primary key
        try:
            Scri.objects.filter(scri=eveid).delete()
        except Exception:
            # Fallback: try deleting by numeric id if legacy model used elsewhere
            try:
                from mainapp.models import Criteria as LegacyCriteria

                LegacyCriteria.objects.filter(id=eveid).delete()
            except Exception:
                pass
    elif ctrl == 'candidates' and eveid:
        # SCandidates has primary key `sconid`
        try:
            SCandidates.objects.filter(sconid=eveid).delete()
        except Exception:
            # Fallback: try legacy Candidate model name if present
            try:
                from mainapp.models import Candidate as LegacyCandidate

                LegacyCandidate.objects.filter(id=eveid).delete()
            except Exception:
                pass
    elif ctrl == 'userespass' and eveid:
        SAdmin.objects.filter(userid=eveid).update(spassword='isu')  # Replace with proper password hashing
    elif ctrl == 'userdelete' and eveid:
        SAdmin.objects.filter(userid=eveid).delete()
    elif ctrl == 'cancelapprove':
        Judgesapproved.objects.all().delete()
    return JsonResponse({'status': 'ok'})
