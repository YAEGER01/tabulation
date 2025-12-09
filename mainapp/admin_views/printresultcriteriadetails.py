
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.html import escape
from django.db.models import Sum
from mainapp.models import Candidate, Event, Judge, Score, Criteria, Approval
import io
# NOTE: Requires reportlab. Install with: pip install reportlab
from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

@login_required
def printresultcriteriadetails(request):
    getevid = request.GET.get('myevid')
    gettitlecri = request.GET.get('mydes')
    getper = request.GET.get('myper')
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="result.pdf"'
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=landscape(A4))
    width, height = landscape(A4)
    y = height - 30
    # Title
    title = f"{gettitlecri} ({getper}%)"
    p.setFont("Times-Bold", 16)
    p.drawCentredString(width/2, y, title)
    y -= 30
    # Table header
    p.setFont("Times-Bold", 10)
    x = 10
    p.drawString(x, y, "Rank")
    x += 40
    p.drawString(x, y, "Candidate #")
    x += 60
    p.drawString(x, y, "Candidate Name")
    x += 120
    # Judges columns
    judges = Judge.objects.filter(event_id=getevid)
    judge_ids = []
    for idx, judge in enumerate(judges, 1):
        p.drawString(x, y, f"Judge {idx}")
        judge_ids.append(judge.id)
        x += 60
    p.drawString(x, y, "Total")
    y -= 20
    # Candidates and scores
    candidates = Candidate.objects.filter(event_id=getevid, canstatus=1).order_by('-approval__inscore')
    for rank, candidate in enumerate(candidates, 1):
        x = 10
        p.setFont("Times-Roman", 10)
        p.drawString(x, y, str(rank))
        x += 40
        p.drawString(x, y, str(candidate.cano))
        x += 60
        p.drawString(x, y, candidate.cname)
        x += 120
        totscore = 0
        cntjude = 0
        for judge_id in judge_ids:
            score = Score.objects.filter(event_id=getevid, candidate=candidate, judge_id=judge_id, criteria__id=gettitlecri).aggregate(total=Sum('inscore'))['total'] or 0
            p.drawString(x, y, str(score))
            totscore += score
            cntjude += 1
            x += 60
        resultscore = round(totscore / cntjude, 2) if cntjude else 0
        p.drawString(x, y, str(resultscore))
        y -= 20
        if y < 50:
            p.showPage()
            y = height - 30
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
