from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    return render(request, "mainPage.html", {})


def about_me_view(request, *args, **kwargs):
    return render(request, "aboutMePage.html", {})


def resume_view(request, *args, **kwargs):
    return render(request, "resumePage.html", {})