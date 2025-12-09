from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from mainapp.models import SCandidates, Scorevents

@csrf_exempt
def addaspirant(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        event_id = request.POST.get('optevent')
        cano = request.POST.get('cano')
        cname = request.POST.get('cname')
        course = request.POST.get('course')
        sconid = request.POST.get('sconid') or request.POST.get('edit_id')
        if category and event_id and cano and cname and course:
            try:
                event = Scorevents.objects.get(evid=event_id)
                if sconid:
                    # Edit existing
                    try:
                        aspirant = SCandidates.objects.get(sconid=sconid)
                        aspirant.evid = event
                        aspirant.cano = cano
                        aspirant.cname = cname
                        aspirant.course = course
                        aspirant.category = category
                        aspirant.canstatus = 1
                        aspirant.save()
                    except SCandidates.DoesNotExist:
                        pass
                else:
                    # New
                    SCandidates.objects.create(
                        evid=event,
                        cano=cano,
                        cname=cname,
                        course=course,
                        category=category,
                        canstatus=1
                    )
            except Scorevents.DoesNotExist:
                pass
        return redirect('/admin/canlst/')
    return redirect('/admin/canlst/')