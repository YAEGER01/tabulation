from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from dbase.models import Judge, Candidate, Criteria, Score

@login_required
def judge_page_criteria(request):
    user = request.user
    judge_id = request.GET.get('myjid')
    cri_id = request.GET.get('mycrid')
    try:
        judge = Judge.objects.get(pk=judge_id)
    except Judge.DoesNotExist:
        return HttpResponseForbidden()
    event = judge.event
    categories = Candidate.objects.filter(evid=event, status=1).values_list('category', flat=True).distinct().order_by('-category')
    criteria = Criteria.objects.filter(pk=cri_id, status=1)
    table_data = []
    for category in categories:
        candidates = Candidate.objects.filter(evid=event, status=1, category=category)
        candidate_rows = []
        for candidate in candidates:
            row = {
                'cano': candidate.cano,
                'cname': candidate.cname,
                'scores': [],
                'total': 0,
                'id': candidate.pk,
            }
            total = 0
            for cri in criteria:
                score_obj = Score.objects.filter(sconid=candidate, scri=cri, ejid=judge).first()
                inscore = score_obj.inscore if score_obj else 0
                total += inscore
                if inscore == 0:
                    rinscore = 'waiting...'
                    inviwait = 'visible'
                else:
                    rinscore = inscore
                    inviwait = 'hidden'
                row['scores'].append({
                    'rinscore': rinscore,
                    'inviwait': inviwait,
                    'crid': cri.pk,
                })
            row['total'] = total
            candidate_rows.append(row)
        table_data.append({
            'category': category,
            'candidates': candidate_rows,
        })
    context = {
        'event': event,
        'judge': judge,
        'criteria': criteria,
        'table_data': table_data,
        'judge_id': judge_id,
        'cri_id': cri_id,
    }
    return render(request, 'judge/judgepagecri.html', context)
