from django.http import HttpResponse
from django.shortcuts import render

def webPage1(request):
    return render(request, 'mainPage.html')

def webPage2(request):
    return render(request, 'resumePage.html')

def webPage3(request):
    return render(request, 'aboutMePage.html')