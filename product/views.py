from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class ProductAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    # Create product
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created'}, 
                            status = status.HTTP_201_CREATED)
        return Response(serializer.errors, 
                        status = status.HTTP_400_BAD_REQUEST)
    
     # Get all products
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductAPIView2(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
     # Retrive a single product
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None: 
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)

    # Complete product update
    def put(self, request, pk, format=None):
        id = pk
        product = Product.objects.get(pk=id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data updated'})
        return Response(serializer.errors, 
                        status = status.HTTP_400_BAD_REQUEST)

    # Partial product update
    def patch(self, request, pk, format=None):
        id = pk
        product = Product.objects.get(pk=id)
        serializer = ProductSerializer(product, data=request.data, 
                                       partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data updated'})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    # Product Delete 
    def delete(self, request, pk, format=None):
        id = pk
        product = Product.objects.get(pk=id)
        product.delete()
        return Response({'msg': 'Data Deleted'}) 
