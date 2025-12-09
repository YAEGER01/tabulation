from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Q
from dbase.models import Judge, Event, Candidate, Criteria, Score

@login_required
def judge_result_table(request):
    user = request.user
    judge_id = request.GET.get('myjid')
    try:
        judge = Judge.objects.get(pk=judge_id)
    except Judge.DoesNotExist:
        return HttpResponseForbidden()
    event = judge.event
    categories = Candidate.objects.filter(evid=event, status=1).values_list('category', flat=True).distinct().order_by('-category')
    criteria = Criteria.objects.filter(evid=event, status=1)
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
                subdon = score_obj.subdon if score_obj else ''
                criper = cri.cper
                total += inscore * (criper / 100)
                if subdon == 'y':
                    rchk = True
                    rnamchk = 'Unlocked'
                    rvalchk = 0
                else:
                    rchk = False
                    rnamchk = 'Locked'
                    rvalchk = 1
                row['scores'].append({
                    'inscore': inscore,
                    'rchk': rchk,
                    'rnamchk': rnamchk,
                    'rvalchk': rvalchk,
                    'crid': cri.pk,
                    'criper': criper,
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
    }
    return render(request, 'judge/judgereset.html', context)

@login_required
def judge_reset_score(request):
    if request.method == 'GET':
        mycontrol = request.GET.get('mycontrol')
        myinscore = request.GET.get('myinscore')
        mycanid = request.GET.get('mycanid')
        mycrid = request.GET.get('mycrid')
        myevid = request.GET.get('myevid')
        myjid = request.GET.get('myjid')
        criper = request.GET.get('criper')
        try:
            score = Score.objects.get(sconid_id=mycanid, scri_id=mycrid, ejid_id=myjid)
            score.subdon = myinscore
            score.save()
            return JsonResponse({'status': 'success'})
        except Score.DoesNotExist:
            return JsonResponse({'status': 'not_found'}, status=404)
    return JsonResponse({'status': 'invalid'}, status=400)
