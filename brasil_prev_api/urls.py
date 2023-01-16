from .routers import api_routers
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="brasil prev API",
        default_version="v1",
    ),
    public=True,
)

# api routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_routers.urls)),
    path('api/v1/docs', schema_view.with_ui('swagger'))
]
