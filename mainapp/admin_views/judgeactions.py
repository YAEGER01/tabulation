from django.shortcuts import render, redirect, get_object_or_404
from mainapp.models import SJudge, Scorevents
import hashlib

def edit_judge(request, judge_id):
    judge = get_object_or_404(SJudge, ejid=judge_id)
    events = Scorevents.objects.all()
    
    if request.method == 'POST':
        judge.jname = request.POST.get('txtname')
        judge.uname = request.POST.get('txtuname')
        event_id = request.POST.get('optevent')
        if event_id:
            judge.evid = Scorevents.objects.get(evid=event_id)
        judge.save()
        return redirect('judgelist')
    
    return render(request, 'judge/edit_judge.html', {'judge': judge, 'events': events})

def delete_judge(request, judge_id):
    judge = get_object_or_404(SJudge, ejid=judge_id)
    # Delete associated scores first
    from mainapp.models import Sinscore
    Sinscore.objects.filter(ejid=judge.ejid).delete()
    judge.delete()
    return redirect('judgelist')

def reset_judge_password(request, judge_id):
    judge = get_object_or_404(SJudge, ejid=judge_id)
    
    if request.method == 'POST':
        password = request.POST.get('txtpassword', '').strip()
        if not password:
            password = 'password'  # default password
        # Hash the password with MD5 (consider using a stronger hash in production)
        md5pass = hashlib.md5(password.encode()).hexdigest()
        judge.spassword = md5pass.encode()
        judge.save()
        return redirect('judgelist')
    
    return render(request, 'judge/reset_judge_password.html', {'judge': judge})
