from django.urls import path
from . import views
from .all_report import attendance_report

app_name='core_sys'
urlpatterns = [
    path('',views.dashbord, name='dash'),
    # path('about/',views.about, name='about'),  
    path('about/',views.dashbord, name='about'), 
    path('members/',views.memberPage, name='members'), 
    path('attendance/',views.attendancePage, name='attendance'), 
    path('report/',views.reportPage, name='report'), 
    path('kikao/',attendance_report, name='kikao'), 


]