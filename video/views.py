from django.shortcuts import render
from django import views
from .models import VideoModel
# Create your views here.

class VideoIndexView(views.View):
	def get(self, request):
		item_video = VideoModel.objects.all()
		context = {'item_video': item_video}
		return render(request, 'video/videoindex.html', context)