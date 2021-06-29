from rest_framework.serializers import Serializer
from rest_framework import serializers
from django.contrib.auth.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password',
        ]

    def create(self, validated_data):
        newUser = User()
        newUser.username = validated_data.get('username')
        newUser.first_name = validated_data.get('first_name')
        newUser.last_name = validated_data.get('last_name')
        newUser.set_password(validated_data.get('password'))
        newUser.save()

        return newUser


class UserCurrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',

        ]