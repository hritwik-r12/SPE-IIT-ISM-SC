from django.shortcuts import render, redirect
from .forms import UserSignUpForm
from django.contrib import messages
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}')
            return redirect('homepage')
    else:
        form = UserSignUpForm()
    context = {'form': form}
    return render(request, 'user/signup.html', context)


def logout(request):
    auth.logout(request)
    messages.warning(request, f'You have been logged out of your current session.')
    return redirect('homepage')


