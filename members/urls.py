from django.urls import path,include
from . import views
# app_name='members'

urlpatterns = [
    path('get_member_data/',views.get_member_data, name='get_member_data'),
    path('add_member/',views.AddMemberByForm, name='add_member'),
    path('upload_member/',views.AddMemberByUpload, name='upload_member'),

]