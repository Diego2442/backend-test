from django.urls import path 
from .views import *

urlpatterns = [
    path('list_product', ListProductoAPIView.as_view()),
    path('create_product', CreateProductoAPIView.as_view()),
    path('update_product/<pk>', UpdateProductoAPIView.as_view()),
    path('delete_product/<pk>', DeleteProductoAPIView.as_view()),
]