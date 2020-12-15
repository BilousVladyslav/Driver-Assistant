from rest_framework import serializers

from .models import Car, Coordinates


class CoordinatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coordinates
        exclude = ['id']


class CarSerializer(serializers.ModelSerializer):
    coordinates = CoordinatesSerializer(read_only=True)

    class Meta:
        model = Car
        fields = '__all__'
        read_only_fields = ['coordinates', 'is_special', 'owner']

    def create(self, validated_data):
        car = Car(**validated_data, owner=self.context['request'].user)
        car.save()
        return car
