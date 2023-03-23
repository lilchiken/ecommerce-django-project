from rest_framework import serializers

from cart.models import (
    Order,
    ProductOrder
)


class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    products = ProductOrderSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
