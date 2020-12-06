"""
Example API endpoint with Swagger documentation:

    class ExampleViewSet(viewsets.ViewSet):

        @swagger_auto_schema(responses=schemas.response_schema_dict)
        def list(self, request):
            '''
            Example API for retrieving users list.

                Access for all.

                Example enum description:
                    IN_PROGRESS = 1
                    REJECTED = 2
                    CLOSED = 3
            '''
            queryset = User.objects.all()
            serializer = UserSerializer(queryset, many=True)
            return Response(serializer.data)
"""
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from . import serializers
from . import swagger_schemas as schemas
from .models import Car, Coordinates


class CarViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin,
                 mixins.UpdateModelMixin, mixins.ListModelMixin):
    serializer_class = serializers.CarSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)

