from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken import views
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema

from .serializers import UserProfileSerializer, RegisterUserSerializer
from .yasg import AuthSwaggerSerializer, auth_swagger_schema


class UserRegistration(GenericViewSet, mixins.CreateModelMixin):
    serializer_class = RegisterUserSerializer

    def post(self, request):
        """
        API for registering new user.

            .
        """
        return self.create(request)


class UserProfile(GenericViewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication, SessionAuthentication, TokenAuthentication]
    serializer_class = UserProfileSerializer
    queryset = get_user_model().objects.all()

    def get_object(self):
        return self.request.user

    def list(self, request, *args, **kwargs):
        """
        API for retrieving user profile.

            .
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        """
        API for updating user profile.

            .
        """
        return super(UserProfile, self).update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        """
        API for partial updating user profile.

            .
        """
        return super(UserProfile, self).partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        """
        API for deleting user profile.

            .
        """
        return super(UserProfile, self).destroy(request, *args, **kwargs)


class ObtainAuthToken(views.ObtainAuthToken):

    @swagger_auto_schema(request_body=AuthSwaggerSerializer(), responses=auth_swagger_schema)
    def post(self, request, *args, **kwargs):
        """
        API for retrieving user auth token.

            .
        """
        return super(ObtainAuthToken, self).post(request, *args, **kwargs)
