from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'project_app/index.html')

def plot(request):
    return render(request, 'project_app/plot.html')

def user_login(request):
    return render(request, 'project_app/user_login.html')

def user_registration(request):
    return render(request, 'project_app/user_registration.html')