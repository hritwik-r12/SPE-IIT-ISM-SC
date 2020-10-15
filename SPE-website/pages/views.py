from django.shortcuts import render


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def profile(request):
    return render(request, 'pages/profile.html')
