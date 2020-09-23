from django.shortcuts import render
from django import views
# Create your views here.

class ProductsView(views.View):
	def get(self, request):
		return render(request, 'products/index.html')