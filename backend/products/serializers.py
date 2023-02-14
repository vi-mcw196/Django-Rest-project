from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    personal_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ['title', 'content', 'price', 'sale_price', 'personal_discount']

    def get_personal_discount(self, obj):
        return obj.get_discount_price()
