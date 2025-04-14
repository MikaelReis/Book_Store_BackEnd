from rest_framework import viewsets
from .models import Product
from .serializers.product_serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer