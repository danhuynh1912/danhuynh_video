from django.shortcuts import render
from django import views
from . import models as images_models
# Create your views here.

class ProductsView(views.View):
	def get(self, request):
		imgs = images_models.ImagesProducts.objects.all()
		context = {'imgs': imgs}
		return render(request, 'products/index.html', context)


class ProductInforView(views.View):
	def get(self, request, thisId):
		infor = images_models.ImagesProducts.objects.get(pk = thisId)
		products = images_models.ImagesProducts.objects.exclude(id = infor.id)
		context = {'infor': infor, 'products': products}
		print(type(products))
		return render(request, 'products/detailthisproduct.html', context)