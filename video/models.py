from django.db import models

# Create your models here.

class VideoModel(models.Model):
	title = models.CharField(max_length=200,null=True, default=None);
	description = models.TextField(max_length=1000,null=True, default=None);
	video = models.FileField(upload_to='video_files', null=True)
	images = models.ImageField(upload_to='videos');
	create_at = models.DateTimeField(null=True, default=None);

	def __str__(self):
		return str(self.title)