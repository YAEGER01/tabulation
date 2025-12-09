from django.shortcuts import render, redirect
from django.db.models import Q, Sum
from mainapp.models import SJudge, Scorevents, SCandidates, Scri, Sinscore, Judgesapproved, Judge
from django.http import HttpResponse

def judge_adminpage(request):
    
    session = request.session
    judgeid = session.get('judgeid') or session.get('ctrlid')
    if not judgeid:
        return redirect('/')
    get_ses = judgeid
    get_name = session.get('logname', '')
    get_idno = request.GET.get('deptid')
    
    try:
        judge = SJudge.objects.select_related('evid').get(ejid=get_ses)
    except SJudge.DoesNotExist:
        return redirect('index')
   
    event = judge.evid  
    evdes = None
    try:
        admin_judge = Judge.objects.filter(uname=judge.uname).first()
    except Exception:
        admin_judge = None

    if admin_judge and getattr(admin_judge, 'event', None):
        
        admin_evt = admin_judge.event
        evdes = getattr(admin_evt, 'evdes', '') or '(No description)'
       
        event = Scorevents.objects.filter(pk=getattr(admin_evt, 'pk', None)).first()
        if not event and getattr(admin_evt, 'evdes', None):
            event = Scorevents.objects.filter(evdes=admin_evt.evdes).first()
        if not event:
            
            event = Scorevents.objects.create(evdes=admin_evt.evdes or '(No description)')
    else:
      
        event = event
        if event:
            evdes = getattr(event, 'evdes', '') or '(No description)'
        else:
            evdes = '(No event assigned)'
    
    categories = SCandidates.objects.filter(evid=event, canstatus='1').values_list('category', flat=True).distinct().order_by('-category')
    
    category_tables = []
    for category in categories:
       
        cri_headers = list(Scri.objects.filter(evid=event, category='1', status='1').values('ctitle', 'scri', 'cper', 'minrate'))
        totcri = sum([c['cper'] for c in cri_headers])
       
        candidates = SCandidates.objects.filter(evid=event, category=category, canstatus='1').order_by('cano')
        candidate_rows = []
        for candidate in candidates:
            row = {
                'cano': candidate.cano,
                'cname': candidate.cname,
                'scores': [],
                'total': 0,
                'sconid': candidate.sconid,
            }
            for cri in cri_headers:
                crid = cri['scri']
                criper = cri['cper']
                crimin = cri['minrate']
               
                sinscore, created = Sinscore.objects.get_or_create(
                    sconid=candidate, evid=event, ejid=judge, scri_id=crid,
                    defaults={'inscore': '0', 'subdon': ''}
                )
               
                try:
                    numeric_inscore = float(sinscore.inscore) if sinscore.inscore not in (None, '') else 0.0
                except Exception:
                    numeric_inscore = 0.0
                recinscore = sinscore.inscore if numeric_inscore > 0 else ''
                ctrldon = sinscore.subdon
                row['scores'].append({
                    'crid': crid,
                    'criper': criper,
                    'crimin': crimin,
                    'inscore': recinscore,
                    'readonly': (ctrldon == 'y' or get_ses == getattr(candidate, 'ejid', None)),
                })
                row['total'] += numeric_inscore
            candidate_rows.append(row)
        category_tables.append({
            'category': category,
            'cri_headers': cri_headers,
            'totcri': totcri,
            'candidates': candidate_rows,
        })
   
    cntrefresh = Sinscore.objects.filter(ejid=get_ses, evid=event, subdon__in=['0', '']).count()
    show_submit = cntrefresh > 0
   
    try:
        
        judge_approved = Judgesapproved.objects.get(ejid=get_ses, evid=getattr(event, 'evid', event))
        apdec = judge_approved.aprem
    except Judgesapproved.DoesNotExist:
        apdec = 'n'
    
    auto_refresh = cntrefresh < 1
    context = {
        'vjname': get_name.upper(),
        'evdes': evdes,
        'category_tables': category_tables,
        'show_submit': show_submit,
        'apdec': apdec,
        'getevid': getattr(event, 'evid', None),
        'getses': get_ses,
        'auto_refresh': auto_refresh,
    }
    return render(request, 'judge/adminpage.html', context)
