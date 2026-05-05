# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('mission-vision/', views.mission_vision, name='mission_vision'),
    path('activities/', views.activities, name='activities'),
    path('donate/', views.donate, name='donate'),
    path('contact/', views.contact, name='contact'),
    path('process-donation/', views.process_donation, name='process_donation'),
    path('donate/charity-to-poor/', views.charity_to_poor, name='charity_to_poor'),
]
