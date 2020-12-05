from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken import views
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, \
    ListModelMixin, CreateModelMixin
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema

from .serializers import UserProfileSerializer, UsersSerializer, RegisterUserSerializer
from .yasg import AuthSwaggerSerializer, auth_swagger_schema


class UserRegistration(GenericViewSet, CreateModelMixin):
    serializer_class = RegisterUserSerializer

    def post(self, request):
        return self.create(request)


class UserProfile(GenericViewSet, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication, SessionAuthentication, TokenAuthentication]
    serializer_class = UserProfileSerializer
    queryset = get_user_model().objects.all()

    def get_object(self):
        return self.request.user


class GetUsersList(GenericViewSet, ListModelMixin):
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
