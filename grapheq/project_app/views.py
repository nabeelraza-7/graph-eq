from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'project_app/index.html')

def plot(request):
    return render(request, 'project_app/plot.html')
