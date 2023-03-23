from datetime import (
    datetime,
    timedelta
)

from rest_framework import viewsets

from api.serializers import OrderSerializer
from cart.models import Order


class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.filter(
        created__gte=datetime.now() - timedelta(hours=1)
    )
    serializer_class = OrderSerializer
