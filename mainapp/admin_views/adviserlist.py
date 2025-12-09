from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from mainapp.models import Gradinsname

@login_required
def adviserlist(request):
    # Query advisers (ulevel = '3')
    advisers = Gradinsname.objects.filter(ulevel='3').order_by('lname', 'fname')
    context = {
        'advisers': advisers,
    }
    return render(request, 'admin/adviserlist.html', context)
