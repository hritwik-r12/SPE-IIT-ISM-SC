from django.shortcuts import render
from .models import Events

# Create your views here.
def home(request):
    context={
        'events': Events.objects.all()
    }
    return render(request, 'events/home.html', context)