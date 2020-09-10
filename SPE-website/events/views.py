from django.shortcuts import render
from .models import Events


def home(request):
    context = {
        'events': Events.objects.all()
    }
    return render(request, 'events/home.html', context)
