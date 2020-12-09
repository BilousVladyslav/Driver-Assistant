from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'first_name', 'last_name']
        read_only_fields = ['username', 'email']


class RegisterUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True, write_only=True, min_length=8)

    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'first_name', 'last_name', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True,
                                     'min_length': 8,
                                     'required': True,
                                     'max_length': 40},
                        'email': {'required': True,
                                  'validators': [UniqueValidator(queryset=get_user_model().objects.all(),
                                                                 message='Email already exist.')]},
                        'last_name': {'required': True},
                        'first_name': {'required': True},
                        'username': {'min_length': 5}}

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError('Passwords must match.')
        attrs.pop('confirm_password')
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        model = get_user_model()
        user = model.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
