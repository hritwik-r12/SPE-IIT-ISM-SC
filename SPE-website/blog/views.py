from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    order_by = ['-date_posted']
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.order_by('-id')


class PostDetailView(DetailView):
    model = Post


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-id')


# figure out pagination and use this as main profile page.
def user_blog(request, username):
    req_user = get_object_or_404(User, username=username)

    posts = req_user.post_set.all().order_by('-id')
    paginator = Paginator(posts, 4)  # Show 4 blogs per page.

    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'req_user': req_user,
        'posts': page_obj,
        # 'page_obj': page_obj,
    }
    return render(request, 'blog/user_posts.html', context)
