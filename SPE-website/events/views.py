from django.shortcuts import render
from .models import Events
from django.views.generic import ListView, DetailView


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
        return Events.objects.order_by('-id')

class EventDetailView(DetailView):
    model = Events