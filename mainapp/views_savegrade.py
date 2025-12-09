from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.db import connection

@csrf_exempt
@require_POST
def save_grade(request):
    getinscode = request.POST.get('myinscode')
    getsubcode = request.POST.get('mysubcode')
    getscheid = request.POST.get('myscheid')
    varusesemid = request.POST.get('mysemid', '').strip()

    
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM essubjectsysem WHERE SubCode=%s AND scheid=%s AND SYID=%s AND InsCode=%s", [getsubcode, getscheid, varusesemid, getinscode])
        qrychecksqlcnt = cursor.rowcount
        cursor.execute("UPDATE essubjectsysem SET submitgrade='yes' WHERE SubCode=%s AND scheid=%s AND SYID=%s AND InsCode=%s", [getsubcode, getscheid, varusesemid, getinscode])

    

    return HttpResponse("<script>alert('Record was successfully saved. SAMPLE'); window.history.back();</script>")
