from django.urls import path
from . import views
from .views import EventListView, EventDetailView

urlpatterns = [
    path('', EventListView.as_view(), name='events-home'),
    path('Event/<int:pk>/', EventDetailView.as_view(), name='events-detail')
]
