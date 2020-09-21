from django.contrib import admin
from django.urls import path
from . import views as core_view

app_name = 'core'

urlpatterns = [
    path('', core_view.IndexView.as_view(), name='home'),
]
