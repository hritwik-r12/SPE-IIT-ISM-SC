from django.urls import path
from . import views
from .views import (
    EventListView, EventDetailView,
    PastEventListView, TeamEventRegisterView,
    EventRegisterView,
)

urlpatterns = [
    path('', EventListView.as_view(), name='events-home'),
    path('past/', PastEventListView.as_view(), name='events-past'),
    path('Event/<int:pk>/', EventDetailView.as_view(), name='events-detail'),
    path('teamRegister/', views.TeamEventRegisterView, name='events-register'),
    path('Register/', views.EventRegisterView, name='events-register')
]
