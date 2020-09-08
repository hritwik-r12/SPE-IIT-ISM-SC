from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    order = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
