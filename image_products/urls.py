from django.urls import path
from . import views as products_view

app_name = 'products'

urlpatterns = [
	path('', products_view.ProductsView.as_view(), name='products')
]