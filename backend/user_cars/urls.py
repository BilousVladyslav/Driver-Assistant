from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('api/my-cars', views.MyCarViewSet, basename='my-cars')
router.register('api/all-cars', views.CarViewSet, basename='all-cars')
router.register('api/coordinates', views.CoordinatesViewSet, basename='coordinates')


urlpatterns = [

]

urlpatterns += router.urls
