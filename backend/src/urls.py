from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from .yasg import urlpatterns as swagger_url

urlpatterns = [
    path('', include('main.urls')),
    path('', include('user_cars.urls')),
    path('jet_api/', include('jet_django.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),

]

urlpatterns += swagger_url

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
