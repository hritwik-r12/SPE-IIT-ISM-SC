from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    UserPostListView,
    user_blog
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
