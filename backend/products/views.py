from api.views import ProductSerializer
from .models import Products
# Create your views here.
from rest_framework import generics, permissions,authentication

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    # permission_classes = [permissions.DjangoModelPermissions]        


# class ProductCreateAPIView(generics.CreateAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer


# class ProductListAPIView(generics.ListCreateAPIView):
#     queryset = Products.objects.all()                                               
#     serializer_class = ProductSerializer

from api.authentication import TokenAuthentication
from .permissions import IsStaffEditorPermission

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Products.objects.all()                                               
    serializer_class = ProductSerializer

    authentication_classes = [
        authentication.SessionAuthentication,
        # authentication.TokenAuthentication  
        TokenAuthentication                                
    ]
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.DjangoModelPermissions] 
    permission_classes = [IsStaffEditorPermission] 
    
    # def perform_update(seld, serializer):
    #     instance = serializer.save()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Products.objects.all()                                               
    serializer_class = ProductSerializer


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Products.objects.all()                                               
    serializer_class = ProductSerializer

#SEE HOW THESE GENERIC API VIEWS INTERNALLY USE GenericApiView + ModelMixins, ctrl + lclick


# Now lets try doing the same thing in one func that will handle and process 
# both get and post requests

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET" , "POST"])
def product_alt_view(request, pk = None, *args, **kwargs):
    method = request.method 

    if method == "GET":
        if pk is not None:
            obj = get_object_or_404(Products, pk = pk)
            data = ProductSerializer(obj, many = False).data

            return Response(data)
        
        queryset = Products.objects.all()
        data = ProductSerializer(queryset, many = True).data
        return Response(data)


    if method == "POST":
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)