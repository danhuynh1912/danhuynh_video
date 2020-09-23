from django.db import models

# Create your models here.

class ImagesProducts(models.Model):
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	theme_image = models.FileField(upload_to='products', null=True)
	create_at = models.DateTimeField(null=True, default=None)


class ImagesDetail(models.Model):
	image = models.FileField(upload_to='DetailImage', null=True, default=None)
	concept = models.ForeignKey('ImagesProducts', on_delete=models.CASCADE)