from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from mainapp.models import Sinscore, Judgesapproved, SCandidates, SJudge, Scorevents, Scri


@require_http_methods(['GET', 'POST'])
def saverecord(request):
   
    data = request.POST if request.method == 'POST' else request.GET
    ctrl = data.get('myctrl')
    if not ctrl:
        return HttpResponse("Invalid control", status=400)

    if ctrl == "inputscore":
        canid = data.get('mycanid', '').strip()
        crid = data.get('mycrid', '').strip()
        evid = data.get('myevid', '').strip()
        jid = data.get('myjid', '').strip()
        inscore = data.get('myinscore', '').strip()
       
        try:
            candidate = SCandidates.objects.filter(sconid=canid).first() if canid else None
            judge = SJudge.objects.filter(ejid=jid).first() if jid else None
            event = Scorevents.objects.filter(evid=evid).first() if evid else None
            scri = Scri.objects.filter(scri=crid).first() if crid else None

           
            obj, created = Sinscore.objects.get_or_create(
                sconid=candidate if candidate else None,
                scri=scri if scri else None,
                evid=event if event else None,
                ejid=judge if judge else None,
                defaults={'inscore': inscore or '0', 'subdon': ''}
            )
            if not created:
                obj.inscore = inscore or '0'
                obj.subdon = ''
                obj.save()
        except Exception as e:
            return HttpResponse(f"ERROR: {e}", status=500)
        return HttpResponse("OK")

    elif ctrl == "submitscore":
        evid = data.get('myevid')
        jid = data.get('myjid')
        try:
            
            judge = SJudge.objects.filter(ejid=jid).first() if jid else None
            event = Scorevents.objects.filter(evid=evid).first() if evid else None
            
            if judge and event:
                Sinscore.objects.filter(ejid=judge, evid=event, inscore__gt=0).update(subdon='y')
            else:
                Sinscore.objects.filter(ejid=jid, evid=evid, inscore__gt=0).update(subdon='y')
        except Exception as e:
            return HttpResponse(f"ERROR: {e}", status=500)
        return HttpResponse("OK")

    elif ctrl == "resapp":
        jid = data.get('myjid')
        try:
            Judgesapproved.objects.filter(ejid=jid).update(aprem='y')
        except Exception as e:
            return HttpResponse(f"ERROR: {e}", status=500)
        return HttpResponse("OK")

    return HttpResponse("Invalid control", status=400)