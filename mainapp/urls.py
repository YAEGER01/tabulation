from .admin_views.judgeactions import edit_judge, delete_judge, reset_judge_password
from .admin_views.judgecrilst import judge_criteria_list
from .admin_views.judgelist import judgelist
from .admin_views.judgepage import judge_page
from django.urls import path
from . import views
from .views_saverecord import saverecord as saverecord_judge
from .views_judge import judge_adminpage
from .views_resultdetails import resultdetails
from .admin_views.adminpage import adminpage
from .admin_views.adminpageres import adminpageres
from .admin_views.adviserlist import adviserlist
from .admin_views.canlst import canlst
from .admin_views.changepass import changepass
from .admin_views.crilst import crilst
from .admin_views.userlist import userlist
from .admin_views.updatehead import updatehead
from .admin_views.saverecord import saverecord as saverecord_admin
from .admin_views.resultsumcandi import resultsumcandi
from .admin_views.resultsum import resultsum
from .admin_views.resultin import resultin
from .admin_views.resultdetails import resultdetails as admin_resultdetails
from .admin_views.resultcriteriadetails import resultcriteriadetails
from .admin_views.resultcriteria import resultcriteria
from .admin_views.resultcrilst import resultcrilst
from .admin_views.resultcontest import resultcontest
from .admin_views.resultcanlst import resultcanlst
from .admin_views.resultcandiindi import resultcandiindi
from .admin_views.resultcandidates import resultcandidates
from .admin_views.result import result, requestapproved, cancelapproved
from .admin_views.resetpass import resetpass
from .admin_views.printresultcriteriadetails import printresultcriteriadetails
from .admin_views.deleterecord import deleterecord
from .admin_views.loginhistory import loginhistory
from .admin_views.editrecord import editrecord
from .admin_views.editcriteria import editcriteria
from .admin_views.eventlst import eventlst
from .admin_views.togglecriteria import togglecriteria
from .admin_views.togglecandidate import toggle_candidate_status, candidate_count

from .admin_views.judgecanlst import judgecanlst, judgecanlst_status
from .admin_views.judgereset import judge_result_table, judge_reset_score
from .admin_views.judgepagecri import judge_page_criteria
from .admin_views.addaspirant import addaspirant
from .admin_views.deleteaspirant import deleteaspirant
path('judge/judgepagecri/', judge_page_criteria, name='judgepagecri'),
from .admin_views.reports import reports_view #dagdag na bago
urlpatterns = [
    path('admin/reports/', reports_view, name='admin_reports'), #dagdag na bago
	path('admin/editcriteria/', editcriteria, name='editcriteria'),
	path('admin/judge/edit/<int:judge_id>/', edit_judge, name='edit_judge'),
	path('admin/judge/delete/<int:judge_id>/', delete_judge, name='delete_judge'),
	path('admin/judge/reset_password/<int:judge_id>/', reset_judge_password, name='reset_judge_password'),
	path('', views.login_view, name='index'),
	# Make Django's default LOGIN_URL (/accounts/login/) resolve to our login_view
	path('accounts/login/', views.login_view, name='accounts_login'),
	path('accounts/logout/', views.logout_view, name='accounts_logout'),
	path('saverecord/', saverecord_judge, name='saverecord'),
    path('judge/adminpage/', judge_adminpage, name='judge_adminpage'),
	path('judge/resultdetails/', resultdetails, name='resultdetails'),
    path('admin/adminpage/', adminpage, name='adminpage'),
	path('admin/adminpageres/', adminpageres, name='adminpageres'),
	path('admin/adviserlist/', adviserlist, name='adviserlist'),
	path('admin/canlst/', canlst, name='canlst'),
	path('admin/changepass/', changepass, name='changepass'),
	path('admin/crilst/', crilst, name='crilst'),
	path('admin/toggle_criteria_status/', togglecriteria, name='toggle_criteria_status'),
	path('admin/toggle_candidate_status/', toggle_candidate_status, name='toggle_candidate_status'),
	path('admin/candidate_count/', candidate_count, name='candidate_count'),
	path('admin/userlist/', userlist, name='userlist'),
	path('admin/updatehead/', updatehead, name='updatehead'),
	path('admin/saverecord/', saverecord_admin, name='admin_saverecord'),
	path('admin/resultsumcandi/', resultsumcandi, name='resultsumcandi'),
	path('admin/resultsum/', resultsum, name='resultsum'),
	path('admin/resultin/', resultin, name='resultin'),
	path('admin/resultdetails/', admin_resultdetails, name='admin_resultdetails'),
	path('admin/resultcriteriadetails/', resultcriteriadetails, name='resultcriteriadetails'),
    path('admin/printresultcriteriadetails/', printresultcriteriadetails, name='printresultcriteriadetails'),
    path('admin/deleterecord/', deleterecord, name='deleterecord'),
	path('admin/resultcriteria/', resultcriteria, name='resultcriteria'),
	path('admin/resultcrilst/', resultcrilst, name='resultcrilst'),
	path('admin/resultcontest/', resultcontest, name='resultcontest'),
	path('admin/resultcanlst/', resultcanlst, name='resultcanlst'),
	path('admin/resultcandidates/', resultcandidates, name='resultcandidates'),
    path('admin/result/', result, name='result'),
    path('admin/requestapproved/', requestapproved, name='requestapproved'),
    path('admin/cancelapproved/', cancelapproved, name='cancelapproved'),
	path('admin/resultcandiindi/', resultcandiindi, name='resultcandiindi'),
		path('admin/resetpass/', resetpass, name='resetpass'),
	path('admin/loginhistory/', loginhistory, name='loginhistory'),
    path('admin/editrecord/', editrecord, name='editrecord'),
    path('admin/eventlst/', eventlst, name='eventlst'),
    path('admin/judgelist/', judgelist, name='judgelist'),
	path('judge/judgecanlst/', judgecanlst, name='judgecanlst'),
	path('judge/judgecanlst_status/', judgecanlst_status, name='judgecanlst_status'),
	path('judge/judgereset/', judge_result_table, name='judgereset'),
	path('judge/judge_reset_score/', judge_reset_score, name='judge_reset_score'),
		path('judge/judgelist/', judgelist, name='judge_judgelist'),
	path('admin/addaspirant/', addaspirant, name='addaspirant'),
	path('admin/deleteaspirant/<int:sconid>/', deleteaspirant, name='deleteaspirant'),
]
