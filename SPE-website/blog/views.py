from django.shortcuts import render

posts = [
    {
        'author': 'Shirin Kaul',
        'title': 'BP-1',
        'content': 'First post content',
        'date_posted': '6 Sept 2020'
    },
    {
        'author': 'XYZ ABC',
        'title': 'BP-2',
        'content': 'Second post content',
        'date_posted': '6 Sept 2020'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)
