from django.shortcuts import render, HttpResponse
import mimetypes


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def gazette(request):
    return render(request, 'pages/gazette.html')
