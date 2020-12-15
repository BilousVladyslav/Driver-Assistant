from drf_yasg import openapi
from rest_framework import serializers

from .serializers import CarSerializer


class CarSwaggerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    number = serializers.CharField(max_length=120)


car_swagger_schema = {
    "201": openapi.Response(
        description="Successful car creating.",
        schema=CarSerializer()
    ),
}


car_edit_swagger_schema = {
    "200": openapi.Response(
        description="Successful car updating.",
        schema=CarSerializer()
    ),
}
