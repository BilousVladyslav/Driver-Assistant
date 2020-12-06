from rest_framework import mixins
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken import views
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema

from .serializers import UserProfileSerializer, UsersSerializer, RegisterUserSerializer
from .yasg import AuthSwaggerSerializer, auth_swagger_schema


class UserRegistration(GenericViewSet, mixins.CreateModelMixin):
    serializer_class = RegisterUserSerializer

    def post(self, request):
        return self.create(request)


class UserProfile(GenericViewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication, SessionAuthentication, TokenAuthentication]
    serializer_class = UserProfileSerializer
    queryset = get_user_model().objects.all()

    def get_object(self):
        return self.request.user

    def list(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class GetUsersList(GenericViewSet, mixins.ListModelMixin):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication, SessionAuthentication, TokenAuthentication]
    serializer_class = UsersSerializer
    queryset = get_user_model().objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['^username', '^first_name', '^last_name']


class ObtainAuthToken(views.ObtainAuthToken):

    @swagger_auto_schema(request_body=AuthSwaggerSerializer(), responses=auth_swagger_schema)
    def post(self, request, *args, **kwargs):
        return super(ObtainAuthToken, self).post(request, *args, **kwargs)
