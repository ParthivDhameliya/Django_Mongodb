from django.shortcuts import render
from .forms import businessPersonRegistration, businessRegistration, businessLogin

# Create your views here.

def home(request):
    return render(request, "business/home.html")

def businessPR(request):
    fm = businessPersonRegistration(auto_id=True, label_suffix=' ')
    return render(request, 'business/businessPersonRegistration.html', {'form':fm})

def businessR(request):
    fm = businessRegistration(auto_id=True, label_suffix=' ')
    return render(request, 'business/businessRegistration.html', {'form':fm})

def businessL(request):
    fm = businessLogin(auto_id=True, label_suffix=' ')
    return render(request, 'business/businessLogin.html', {'form':fm})
