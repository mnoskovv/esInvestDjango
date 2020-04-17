""" URL patterns for profileApp """

from . import views
from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView

from esInvestApp.views import index

urlpatterns = [
    path('login/', LoginView.as_view(template_name="profileApp/login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    # path('register/', views.register, name="register"),
    path('register/', index, name="register"),
]