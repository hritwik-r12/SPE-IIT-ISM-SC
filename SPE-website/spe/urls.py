"""spe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from user import views as user_views
from pages import views as pages_views
from blog import views as blog_views
# to display static files during dev, change when in production.
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('AboutUs/', pages_views.about, name='about-page'),
    path('Blogs/', include('blog.urls')),
    path('SignUp/', user_views.CreateUserView.as_view(template_name='user/signup.html'), name='signup-page'),
    path('SignIn/', auth_views.LoginView.as_view(template_name='user/signin.html'), name='signin-page'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'), name='password_reset'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('password-reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
    path('SignOut/', user_views.logout, name='signout-page'),
    path('Events/', include('events.urls')),
    path('Gallery/', pages_views.gallery, name='gallery-page'),
    path('CoreTeam/', pages_views.core_team, name='core-team'),
    path('markdownx/', include('markdownx.urls')),
    path('user/<str:username>/', blog_views.user_blog, name='user-posts')
]

# only works in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
