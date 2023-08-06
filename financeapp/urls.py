
from django.urls import path
from . import views

app_name = 'financeapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]
