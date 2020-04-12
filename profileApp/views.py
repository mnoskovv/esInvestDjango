from django.shortcuts import render
from django.contrib.auth.views import LogoutView
# Create your views here.

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('esInvestApp:index'))