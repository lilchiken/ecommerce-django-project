from ast import literal_eval

from rest_framework import serializers

from cart.models import Order


class OrderSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Order."""

    products = serializers.SerializerMethodField('get_products')

    class Meta:
        model = Order
        fields = '__all__'

    def get_products(self, obj):
        return literal_eval(obj.products)
