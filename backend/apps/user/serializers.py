from rest_framework import serializers

from user.models import UserProfile
from location.serializers import CitySerializer
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username")


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    city = CitySerializer(many=False, read_only=True)

    class Meta:
        model = UserProfile
        fields = ("id", "user", "city")
