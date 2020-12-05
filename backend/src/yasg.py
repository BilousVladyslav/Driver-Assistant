from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth.decorators import login_required


schema_view = get_schema_view(
    openapi.Info(
        title="Driver Assistant API",
        default_version='v1',
    ),
    public=True,
)

urlpatterns = [
    path('swagger/', login_required(schema_view.with_ui('swagger', cache_timeout=0)), name='schema-swagger-ui'),
]
