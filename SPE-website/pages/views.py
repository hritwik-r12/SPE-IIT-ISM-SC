from django.shortcuts import render


def home(request):
    return render(request, 'pages/blog-page.html')
