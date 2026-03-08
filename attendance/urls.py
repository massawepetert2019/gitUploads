from django.urls import path
from . import views


urlpatterns = [   
    path('', views.homePage),
    path('take_attendance', views.take_attendance, name='take_attendance'),

]