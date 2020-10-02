from django.urls import path
from . import views
from .views import (
    EventListView, EventDetailView,
    PastEventListView, EventRegisterView,
)

urlpatterns = [
    path('', EventListView.as_view(), name='events-home'),
    path('past/', PastEventListView.as_view(), name='events-past'),
    path('Event/<int:pk>/', EventDetailView.as_view(), name='events-detail'),
    path('Event/<int:pk>/register', views.EventRegisterView, name='events-register')
]
