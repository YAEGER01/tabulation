from django.views.decorators.http import require_GET
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.hashers import make_password
from mainapp.models import SJudge, SCandidates, Scorevents, Scri, SAdmin, Judgesapproved, Gradinsname

@require_GET
def saverecord(request):
    ctrl = request.GET.get('mycontrol')
    subctrl = request.GET.get('mysubctrl')
    # Only a subset of cases are implemented for brevity. Add more as needed.
    if ctrl == "judge":
        jname = request.GET.get('myjname', '').strip()
        juname = request.GET.get('myuname', '').strip()
        jpass = make_password(request.GET.get('myjpass', '').strip())
        jcateg = request.GET.get('myjcateg', '').strip()
        eve = request.GET.get('myeve', '').strip()
        if not SJudge.objects.filter(uname=juname).exists():
            SJudge.objects.create(evid=eve, jname=jname, uname=juname, category=jcateg, spassword=jpass)
        return JsonResponse({'success': True})
    elif ctrl == "candidates":
        cano = request.GET.get('mycano', '').strip()
        caname = request.GET.get('mycaname', '').strip()
        course = request.GET.get('mycourse', '').strip()
        categ = request.GET.get('mycateg', '').strip()
        eve = request.GET.get('myeve', '').strip()
        if categ == "select":
            categ = ""
        if not SCandidates.objects.filter(cname=caname).exists():
            SCandidates.objects.create(evid=eve, cano=cano, cname=caname, course=course, category=categ)
        return JsonResponse({'success': True})
    # ...implement other cases as needed...
    return HttpResponse("Not implemented", status=501)
