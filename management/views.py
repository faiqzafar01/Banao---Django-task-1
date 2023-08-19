from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from management.models import *

# Create your views here.

def dashboard_view(request):
    return render(request, 'index.html')

def signup_view(request):
    return render(request, 'signup.html')

def login_view(request):
    return render(request, 'login.html')



def Doctor_view(request):
    return HttpResponse("<center><h1>Hey This page is only for doctor</h1></center>")


def Patient_view(request):
    return HttpResponse("<center><h1>Hey This page is only for Patient</h1></center>")
