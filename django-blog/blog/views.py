from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return HttpResponse("Home Page")

def about(request):
    return render(request,'about.html')
