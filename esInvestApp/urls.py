""" URL patterns for esInvestApp """

from . import views
from django.urls import path

urlpatterns = [
        path('', views.index, name = 'index'),
        path('profile/', views.profile, name = 'profile'),
        path('profile/open_deal', views.open_deal, name='open_deal'),
        path('profile/start', views.start, name='start'),
        path('about/', views.about, name='about'),
]