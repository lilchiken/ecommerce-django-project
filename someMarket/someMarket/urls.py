from django.contrib import admin
from django.urls import (
    path,
    include,
    re_path
)
from django.views.generic import TemplateView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="someMarket API",
        default_version='v1',
    ),
    patterns=[path('api/', include('api.urls')), ],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(
        'docs/',
        TemplateView.as_view(
            template_name='swaggerui/swaggerui.html',
            extra_context={'schema_url': 'openapi-schema'}
        ),
        name='swagger-ui'
    ),
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(),
        name='schema-json'
    ),
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('cart/', include('cart.urls')),
    path('api/', include('api.urls'))
]
