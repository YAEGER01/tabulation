from django.shortcuts import render, redirect
from django.db.models import Sum
from mainapp.models import SCandidates, Scorevents, SJudge, Sinscore, Scri


def resultcandidates(request):
    # Session-based admin check
    if not request.session.get('ctrlid'):
        return redirect('index')

    getidcri = request.GET.get('myeveid')
    gettitlecri = request.GET.get('mydes')
    getper = request.GET.get('myper')

    # Find the Scri/criterion
    scri = Scri.objects.filter(scri=getidcri).first() if getidcri else None

    # If a specific criterion id is provided, limit to its event only
    if getidcri:
        scri = Scri.objects.filter(scri=getidcri).first()
        events = [scri.evid] if scri and scri.evid else []
    else:
        events = Scorevents.objects.all().order_by('evid')
    event_data = []
    for event in events:
        # Judges and candidates for this event
        judges = SJudge.objects.filter(evid=event)
        candidates = SCandidates.objects.filter(evid=event, canstatus='1')

        # Candidate totals for this criterion (prefetch sinscore rows)
        candidate_scores = []
        sins_for_event = Sinscore.objects.filter(evid_id=event.evid, scri_id=getidcri)
        score_map = {}
        for s in sins_for_event:
            key = (getattr(s, 'sconid_id', None), getattr(s, 'ejid_id', None), getattr(s, 'scri_id', None))
            score_map[key] = s.inscore
        for candidate in candidates:
            total_score = 0.0
            # Sum Sinscore values for this candidate across judges
            for s in [v for k,v in score_map.items() if k[0] == candidate.sconid and k[2] == int(getidcri)]:
                try:
                    if s not in (None, ''):
                        total_score += float(s)
                except Exception:
                    pass
            candidate_scores.append({'candidate': candidate, 'total_score': total_score})

        # For each judge, build row of scores for display
        judge_rows = []
        for idx, judge in enumerate(judges, 1):
            row = {'number': idx, 'scores': []}
            for candidate in candidates:
                key = (candidate.sconid, judge.ejid, int(getidcri))
                s_ins = score_map.get(key, None)
                score = s_ins if s_ins not in (None, '') else None
                row['scores'].append({'score': score if score is not None else 'waiting', 'waiting': score is None})
            judge_rows.append(row)

        totals = []
        for candidate in candidates:
            total = 0.0
            for k, v in score_map.items():
                if k[0] == candidate.sconid and k[2] == int(getidcri):
                    try:
                        if v not in (None, ''):
                            total += float(v)
                    except Exception:
                        pass
            totals.append(total)

        event_data.append({
            'event': event,
            'criteria_title': gettitlecri,
            'criteria_percent': getper,
            'candidates': list(candidates),
            'judges': list(judges),
            'judge_rows': judge_rows,
            'totals': totals,
        })

    return render(request, 'admin/resultcandidates.html', {'event_data': event_data, 'criteria_title': gettitlecri, 'criteria_percent': getper})
