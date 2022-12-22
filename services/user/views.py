from django.shortcuts import render
from .forms import userLogin, userRegistration
# Create your views here.

def home(request):
    return render(request, 'user/home.html')

def userR(request):
    fm = userRegistration(auto_id=True, label_suffix=' ')
    return render(request, 'user/userRegistration.html', {'form':fm})

def userL(request):
    fm = userLogin(auto_id=True, label_suffix=' ')
    return render(request, 'user/userLogin.html', {'form':fm})