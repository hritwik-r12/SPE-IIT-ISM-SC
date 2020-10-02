from django.shortcuts import render, get_object_or_404
from .models import Events, Registeration
from django.views.generic import ListView, DetailView
import datetime
from .forms import RegisterForm


def home(request):
    context = {
        'events': Events.objects.all()
    }
    return render(request, 'events/home.html', context)

class EventListView(ListView):
    model = Events
    template_name = 'events/home.html'
    context_object_name = 'events'
    order_by = ['-reg_date']
    paginate_by = 3

    def get_queryset(self):
        date_1=datetime.date.today()
        #Positivly update by 2040!
        return Events.objects.filter(reg_date__lte=datetime.date(2040,1,1),
                                     reg_date__gte=date_1).order_by('-id')

class EventDetailView(DetailView):
    model = Events

class PastEventListView(ListView):
    model = Events
    template_name = 'events/home.html'
    context_object_name = 'events'
    order_by = ['-reg_date']
    paginate_by = 3

    def get_queryset(self):
        date_1=datetime.date.today()
        date_1=date_1 + datetime.timedelta(days=-1)
        return Events.objects.filter(reg_date__lte=date_1,
                                     reg_date__gte=datetime.date(2019,1,1)).order_by('-id')

def EventRegisterView(request, pk):
    r_form = RegisterForm()

    context={
        'r_form': r_form
    }
    return render(request, 'events/registration_details.html', context)