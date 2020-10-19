from django.urls import path
from . import views as products_view

app_name = 'products'

urlpatterns = [
	path('', products_view.ProductsView.as_view(), name='products'),
	path('information-product/<int:thisId>', products_view.ProductInforView.as_view(), name='productsInfor'),
]