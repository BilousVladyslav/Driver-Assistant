from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('api/cars', views.CarViewSet, basename='cars')


urlpatterns = [

]

urlpatterns += router.urls
