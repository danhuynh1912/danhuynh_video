from django.urls import path
from . import views as video_views

app_name = 'video'

urlpatterns = [
	path('video/', video_views.VideoIndexView.as_view(), name='video'),
]