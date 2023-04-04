from datetime import (
    datetime,
    timedelta
)

from rest_framework import viewsets

from api.serializers import OrderSerializer
from cart.models import Order


class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для модели Order."""

    serializer_class = OrderSerializer

    def get_queryset(self):
        """Определение кверисета для разных запросов."""

        if self.kwargs.get('pk'):
            return Order.objects.filter(id=self.kwargs.get('pk'))
        return Order.objects.filter(
            created__gte=datetime.now() - timedelta(hours=1)
        )
