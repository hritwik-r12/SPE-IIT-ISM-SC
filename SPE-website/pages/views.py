from django.shortcuts import render, HttpResponse
import mimetypes


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def gazette(request):
    return render(request, 'pages/gazette.html')


def gallery(request):
    return render(request, 'pages/gallery.html')


def core_team(request):
    return render(request, 'pages/core-team.html')


def contact_us(request):
    return render(request, 'pages/contact-us.html')