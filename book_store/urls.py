
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
schema_view = get_schema_view(
    openapi.Info(
        title="Book Store API",
        default_version='v1',
        description="API for Book Store",
     

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    # url='http://127.0.0.1:8000/api/',
    # patterns=[path('api/', include('books.api.urls'))]


)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    
]

if settings.SHOW_SWAGGER:
    urlpatterns += [
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ]