from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Post API",
        default_version='v1',
        description="API for movies",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@movies.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    # permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('tour/', include('apps.tour.urls')),
    path('location/', include('apps.location_info.urls')),
    path('user/', include('apps.user.urls')),
    path('tags/', include('apps.tags.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
