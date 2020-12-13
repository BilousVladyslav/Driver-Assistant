from django.db.models.query import Q
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from drf_yasg.utils import swagger_auto_schema

from . import serializers
from .models import Car
from .yasg import CarSwaggerSerializer, car_swagger_schema, car_edit_swagger_schema


class MyCarViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                   mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin):
    serializer_class = serializers.CarSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        """
        API for retrieving list of user cars.

            .
        """
        return super(MyCarViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        API for retrieving data about car.

            .
        """
        return super(MyCarViewSet, self).retrieve(request, *args, **kwargs)

    @swagger_auto_schema(request_body=CarSwaggerSerializer(), responses=car_swagger_schema)
    def create(self, request, *args, **kwargs):
        """
        API for creating record about car.

            .
        """
        return super(MyCarViewSet, self).create(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        """
        API for deleting information about user car.

            .
        """
        return super(MyCarViewSet, self).destroy(request, *args, **kwargs)

    @swagger_auto_schema(request_body=CarSwaggerSerializer(), responses=car_edit_swagger_schema)
    def update(self, request, *args, **kwargs):
        """
        API for updating data about user car.

            .
        """
        return super(MyCarViewSet, self).update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=CarSwaggerSerializer(), responses=car_edit_swagger_schema)
    def partial_update(self, request, *args, **kwargs):
        """
        API for partial updating data about user car.

            .
        """
        return super(MyCarViewSet, self).partial_update(request, *args, **kwargs)


class CarViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = serializers.CarSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication, TokenAuthentication]

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return Car.objects.filter(is_special=True)
        else:
            return Car.objects.filter(Q(owner=self.request.user) | Q(is_special=True))
    
    def list(self, request, *args, **kwargs):
        """
        API for retrieving list of user cars and special cars.

            .
        """
        return super(CarViewSet, self).list(request, *args, **kwargs)


class CoordinatesViewSet(viewsets.GenericViewSet, mixins.UpdateModelMixin):
    serializer_class = serializers.CoordinatesSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Car.objects.all()

    def get_object(self):
        car = super(CoordinatesViewSet, self).get_object()
        return car.coordinates
    
    def update(self, request, *args, **kwargs):
        """
        API for updating car coordinates.

            Expects car id.
        """
        return super(CoordinatesViewSet, self).update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        """
        API for partial updating car coordinates.

            .
        """
        return super(CoordinatesViewSet, self).partial_update(request, *args, **kwargs)
