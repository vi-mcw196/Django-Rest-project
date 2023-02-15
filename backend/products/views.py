from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data['title']
        content = serializer.validated_data['content'] or None
        if content is None:
            content = title
        serializer.save(content=content)
        # Here you can send a Django signal to update the database.


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
