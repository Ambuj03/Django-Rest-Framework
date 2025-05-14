from api.views import ProductSerializer
from .models import Products
# Create your views here.
from rest_framework import generics

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer