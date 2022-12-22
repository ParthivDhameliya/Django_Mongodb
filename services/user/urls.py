from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="userhome"),
    path('userLogin/', views.userL, name='userLogin'),
    path('userRegistration/', views.userR, name='userRegistration'),
]
