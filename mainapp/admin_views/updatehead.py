from django.views.decorators.http import require_POST
from django.http import JsonResponse
from mainapp.models import Gradinsname
from django.contrib.auth.hashers import make_password

@require_POST
def updatehead(request):
    varid = request.POST.get('idno', '').strip()
    varlname = request.POST.get('lname', '').strip()
    varfname = request.POST.get('fname', '').strip()
    varmname = request.POST.get('mname', '').strip()
    vardeptname = request.POST.get('deptname', '').strip()
    varnpass = request.POST.get('npass', '').strip()
    errors = {}
    if not varid:
        errors['idno'] = 'ID required field!'
    if not varlname:
        errors['lname'] = 'Last name required field!'
    if not varfname:
        errors['fname'] = 'First name required field!'
    if not varmname:
        errors['mname'] = 'Middle name required field!'
    if vardeptname == 'Select' or not vardeptname:
        errors['deptname'] = 'Department required field!'
    if not varnpass:
        errors['npass'] = 'Password required field!'
    if errors:
        return JsonResponse({'success': False, 'errors': errors})
    try:
        gradins = Gradinsname.objects.get(id=varid)
        gradins.lname = varlname
        gradins.fname = varfname
        gradins.mname = varmname
        gradins.department = vardeptname
        gradins.spassword = make_password(varnpass)
        gradins.save()
        return JsonResponse({'success': True, 'message': 'Record was successfully updated'})
    except Gradinsname.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Record not found'})
