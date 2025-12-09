from django.shortcuts import render, redirect

def reports_view(request):
    
    session = request.session
    if not session.get('logid') or not session.get('ctrlid'):
        return redirect('/')

    # Your reports logic here
    context = {
        # Add your context data
    }
    return render(request, 'admin/reports.html', context)