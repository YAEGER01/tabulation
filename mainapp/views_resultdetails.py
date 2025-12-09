from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F, Q
from mainapp.models import Scorevents, Scri, SCandidates, Sinscore, SJudge
from django.http import HttpResponse

@login_required
def resultdetails(request):
    get_ses = request.user.username  
    getevidload = request.GET.get('myevid')
    
    try:
        event = Scorevents.objects.get(evid=getevidload)
    except Scorevents.DoesNotExist:
        return redirect('index')
    evdes = event.evdes
    
    categories = SCandidates.objects.filter(evid=event).values_list('category', flat=True).distinct().order_by('-category')
    
    judges = list(SJudge.objects.filter(evid=event))
    
    totper = Scri.objects.filter(evid=event).aggregate(totper=Sum('cper'))['totper'] or 0
    
    category_tables = []
    for category in categories:
        
        candidates = SCandidates.objects.filter(evid=event, category=category, canstatus='1').order_by('cano')
        candidate_rows = []
        rank = 0
        
        candidate_scores = []
        for candidate in candidates:
            
            total_score = Sinscore.objects.filter(evid=event, sconid=candidate.sconid).aggregate(total=Sum('inscore'))['total'] or 0
            candidate_scores.append((candidate, total_score))
        
        candidate_scores.sort(key=lambda x: x[1], reverse=True)
        for candidate, total_score in candidate_scores:
            rank += 1
            row = {
                'rank': rank,
                'cano': candidate.cano,
                'cname': candidate.cname,
                'judge_scores': [],
                'total': 0,
                'average': 0,
                'grade_score': 0,
            }
            totscore = 0
            cntjude = 0
            for judge in judges:
               
                judge_score = Sinscore.objects.filter(evid=event, sconid=candidate.sconid, ejid=judge.ejid).aggregate(totjudge=Sum('inscore'))['totjudge'] or 0
                row['judge_scores'].append(judge_score)
                totscore += judge_score
                cntjude += 1
            restotscore = totscore / cntjude if cntjude else 0
            totave = ((restotscore / totper) * 50) + 50 if totper else 0
            row['total'] = '{:.2f}'.format(restotscore)
            row['average'] = '{:.2f}'.format(restotscore)
            row['grade_score'] = '{:.2f}'.format(totave)
            candidate_rows.append(row)
        category_tables.append({
            'category': category,
            'judges': judges,
            'candidates': candidate_rows,
        })
    context = {
        'evdes': evdes,
        'category_tables': category_tables,
        'getevid': event.evid,
        'getses': get_ses,
    }
    return render(request, 'judge/resultdetails.html', context)
