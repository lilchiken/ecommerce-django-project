from django.urls import (
    path,
    include
)
from rest_framework.routers import DefaultRouter

from api.views import OrderViewSet

api_v1 = DefaultRouter()
api_v1.register('order', OrderViewSet)

urlpatterns = [
    path('v1/', include(api_v1.urls)),
]