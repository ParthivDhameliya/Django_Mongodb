from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import userLogin, userRegistration
# Create your views here.

def home(request):
    return render(request, 'user/home.html')

def userR(request):
    if request.method == 'POST':
        fm = userRegistration(request.POST)
        if fm.is_valid():
            fm = fm.cleaned_data
            return HttpResponseRedirect('/user/userLogin/')
    else:
        fm = userRegistration(auto_id=True, label_suffix=' ')
    return render(request, 'user/userRegistration.html', {'form':fm})

def userL(request):
    fm = userLogin(auto_id=True, label_suffix=' ')
    return render(request, 'user/userLogin.html', {'form':fm})