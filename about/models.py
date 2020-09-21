from django.db import models

# Create your models here.

class AboutMeModel(models.Model):
	name = models.CharField(max_length=40);
	english_name = models.CharField(max_length=40);
	age = models.IntegerField(default=0);
	description = models.TextField(null=True, default=None);
	images = models.ImageField(upload_to='About');

	def __str__(self):
		return str(self.name)