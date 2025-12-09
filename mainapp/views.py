from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.db import connection
from django.http import HttpRequest, HttpResponse

@csrf_protect
def login_view(request: HttpRequest):
	print(f"DEBUG: login_view called with method={request.method}")
	msguid = ""
	msgpass = ""
	message = ""
	if request.method == "POST":
		username = request.POST.get("username", "").strip()
		password = request.POST.get("cpass", "").strip()
		#print(f"DEBUG: POST data received - username={username}, password={password}")
		#print(f"DEBUG: All POST data: {dict(request.POST)}")
		if not username:
			msguid = "Username field is required."
		if not password:
			msgpass = "Password field is required."
		if username and password:
			import hashlib
			md5pass = hashlib.md5(password.encode()).hexdigest()
			#print(f"DEBUG: md5pass={md5pass}")
			
			with connection.cursor() as cursor:
				cursor.execute("SELECT * FROM sjudge WHERE uname=%s AND spassword=%s", [username, md5pass.encode()])
				judge = cursor.fetchone()
				#print(f"DEBUG: judge result={judge}")
			if judge:
				
				request.session['judgeid'] = judge[0]  
				request.session['categ'] = judge[2]    
				request.session['ctrlid'] = judge[0]
				request.session['logname'] = judge[1]  
				
				return redirect('/judge/adminpage/')
			else:
				
				with connection.cursor() as cursor:
					cursor.execute("SELECT * FROM sadmin WHERE username=%s AND spassword=%s", [username, md5pass.encode()])
					admin = cursor.fetchone()
					#print(f"DEBUG: admin result={admin}")
				if admin:
					request.session['logname'] = admin[1]  
					request.session['logpass'] = password
					request.session['logid'] = admin[0]
					request.session['ctrlid'] = admin[0] 
					varulevel = admin[3] 
					
					return redirect('/admin/adminpage/')
				else:
					message = f"Invalid account, Please try again! (DEBUG: username={username}, md5pass={md5pass})"
	context = {
		'msguid': msguid,
		'msgpass': msgpass,
		'message': message,
		'today': request.GET.get('today', None),
	}
	return render(request, 'index.html', context)

from datetime import date

def index(request):
	today = date.today().strftime("%B %d, %Y")
	return render(request, 'index.html', {'today': today})


def logout_view(request):
	# Clear legacy session keys used by the app
	for k in ['judgeid', 'ctrlid', 'logname', 'categ', 'logid', 'logpass']:
		try:
			del request.session[k]
		except KeyError:
			pass
	return redirect('index')
