from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from mainapp.models import Scri, Scorevents, Event

@csrf_exempt
def editcriteria(request):
    session = request.session
    if not session.get('logid') or not session.get('ctrlid'):
        return redirect('/')

    events = Event.objects.all()

    if request.method == 'POST':
        event_id = request.POST.get('optevent')
        ctitle = request.POST.get('ctitle')
        cper = request.POST.get('cper')
        scri_id = request.POST.get('scri_id')
        status = '1' if request.POST.get('status') == '1' else '0'
        category = '1' if request.POST.get('category') == '1' else '0'
        minrate = request.POST.get('minrate') or ''
        print('DEBUG: POST event_id:', event_id, 'ctitle:', ctitle, 'cper:', cper, 'scri_id:', scri_id, 'status:', status, 'category:', category, 'minrate:', minrate)
        if event_id and event_id != 'None' and ctitle and cper:
            try:
                scorevent = Scorevents.objects.get(evid=event_id)
                if scri_id:
                    # Edit existing
                    scri = Scri.objects.get(pk=scri_id)
                    scri.evid = scorevent
                    scri.ctitle = ctitle
                    scri.cper = cper
                    scri.status = status
                    scri.category = category
                    scri.minrate = minrate
                    scri.save()
                    print('DEBUG: Updated Scri:', scri.pk)
                else:
                    # New
                    scri = Scri.objects.create(
                        evid=scorevent,
                        ctitle=ctitle,
                        cper=cper,
                        status=status,
                        category=category,
                        minrate=minrate
                    )
                    print('DEBUG: Created Scri:', scri.pk)
            except (Scorevents.DoesNotExist, Scri.DoesNotExist) as e:
                print('DEBUG: Exception:', e)
        else:
            print('DEBUG: Did not save, missing required fields')
        return redirect('/admin/crilst/')

    # If GET, render a minimal form (not used by modal, but for completeness)
    return render(request, 'admin/crilst.html', {'events': events})
