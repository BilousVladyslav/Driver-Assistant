from drf_yasg import openapi
from rest_framework import serializers


class AuthSwaggerSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=120)
    password = serializers.CharField(max_length=120)


class TokenSwaggerSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=120)


auth_swagger_schema = {
    "200": openapi.Response(
        description="Successful token retrieving.",
        schema=TokenSwaggerSerializer()
    ),
}
