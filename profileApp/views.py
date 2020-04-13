from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.db import transaction
from .forms import ProfileForm, SignUpForm
from .models import Profile
# Create your views here.

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('esInvestApp:index'))

@transaction.atomic
def register(request):
    if request.method != 'POST':
        register_form = SignUpForm()
        profile_form = ProfileForm()
    else:
        register_form = SignUpForm(data = request.POST)
        if register_form.is_valid():
            new_user = register_form.save()
            authenticated_user = authenticate(username = new_user.username, password = request.POST['password1'])
            login(request, authenticated_user)
            profile_form = ProfileForm(request.POST, instance = authenticated_user.profile)
            if profile_form.is_valid():
                profile_form.save()
            return HttpResponseRedirect(reverse('esInvestApp:index'))

    context = {
        'register_form' : register_form,
        'profile_form': profile_form,
        }
    return render(request, 'profileApp/register.html', context)