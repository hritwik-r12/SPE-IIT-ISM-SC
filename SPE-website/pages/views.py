from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .forms import MessagesForUsForm
import mimetypes


def landing_page(request):
    return render(request, 'pages/landing-page.html')


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
    if request.method == 'POST':
        form = MessagesForUsForm(request.POST)
        if form.is_valid():
            messageforus = form.save()
            messages.success(request, f'Message sent!')
            return redirect('contact-page')
    else:
        form = MessagesForUsForm()
    context = {'form': form}
    return render(request, 'pages/contact-us.html', context)
