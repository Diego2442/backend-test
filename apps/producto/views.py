from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)

from .serializers import ProductoSerializer
from .models import Producto


class ListProductoAPIView(ListAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()


class CreateProductoAPIView(CreateAPIView):
    serializer_class = ProductoSerializer

class UpdateProductoAPIView(RetrieveUpdateAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()


class DeleteProductoAPIView(DestroyAPIView):
    queryset = Producto.objects.all()
