from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

def index(request):
    if(request.POST):
        return render(request, 'pages/home.html')
    return render(request, 'index.html')

def home(request):
    return render(request, 'pages/home.html')
