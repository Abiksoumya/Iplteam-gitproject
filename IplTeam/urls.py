
from django import views
from django.urls import path
from IplTeam import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
]
