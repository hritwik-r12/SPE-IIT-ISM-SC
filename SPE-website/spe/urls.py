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
    path('', pages_views.landing_page, name='landing-page'),
    path('Home/', pages_views.home, name='home-page'),
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
    path('Gallery/', pages_views.tgal, name='gallery-page'),
    path('tgal/', pages_views.tgal, name='tgal-page'),
    path('tgal2/', pages_views.tgal2, name='tgal2-page'),
    path('intern/', pages_views.intern, name='intern-page'),
    path('teacher/', pages_views.teacher, name='teacher-page'),
    path('fipi/', pages_views.fipi, name='fipi-page'),
    path('basant/', pages_views.basant, name='basant-page'),
    path('cdd/', pages_views.cdd, name='cdd-page'),
    path('hall/', pages_views.hall, name='hall-page'),
    path('m/', pages_views.m, name='m-page'),
    path('Gazette/', pages_views.gazette, name='gazette-page'),
    path('CoreTeam/', pages_views.core_team, name='core-team'),
    path('ContactUs/', pages_views.contact_us, name='contact-page'),
    path('markdownx/', include('markdownx.urls')),
    path('user/<str:username>/', blog_views.user_blog, name='user-posts'),
]

# only works in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
