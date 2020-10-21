from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import UserProfile


'''def signup(request):
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
    return render(request, 'user/signup.html', context)'''


def logout(request):
    auth.logout(request)
    messages.warning(request, f'You have been logged out of your current session.')
    return redirect('homepage')

class CreateUserView( SuccessMessageMixin, CreateView):
    success_url= reverse_lazy('signin-page')
    form_class=CreateUserForm
    template_name = 'user/signup.html'

    def form_valid(self, form):
        c = {'form': form,}
        user =form.save(commit=False)
        institute_registration_number = form.cleaned_data['IIT_ISM_registration_number']
        SPE_ID = form.cleaned_data['spe_id']
        password = form.cleaned_data['password']
        repeat_password = form.cleaned_data['repeat_password']
        if password != repeat_password:
            messages.error(self.request, "Passwords do not Match", extra_tags='alert alert-danger')
            return render(self.request, self.template_name, c)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, institute_registration_number=institute_registration_number, SPE_ID=SPE_ID)
 
        return super(CreateUserView, self).form_valid(form)