from django.contrib import admin 
from django.urls import path
from . import views as views_about

app_name = 'about'

urlpatterns = [
    path('about/', views_about.AboutMeView.as_view(), name="aboutme"),
]