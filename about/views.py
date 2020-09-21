from django.shortcuts import render
from django import views
from .models import AboutMeModel
# Create your views here.

class AboutMeView(views.View):
    def get(self, request):
        about_me = AboutMeModel.objects.all()
        return render(request, 'about/about.html', {'me': about_me})
        