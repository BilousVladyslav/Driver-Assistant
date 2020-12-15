from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('api/register', views.UserRegistration, basename='register')
router.register('api/profile', views.UserProfile, basename='profile')


urlpatterns = [
    path('', login_required(RedirectView.as_view(pattern_name='admin:index'))),
    path('api/auth/', views.ObtainAuthToken.as_view())
]

urlpatterns += router.urls
