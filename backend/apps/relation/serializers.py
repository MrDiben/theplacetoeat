from rest_framework import serializers

from relation.models import FriendShip
from user.serializers import UserProfileSerializer


class FriendShipSerializer(serializers.ModelSerializer):
    user_1 = UserProfileSerializer(many=False, read_only=True)
    user_2 = UserProfileSerializer(many=False, read_only=True)

    class Meta:
        model = FriendShip
        fields = ("id", "user_1", "user_2", "status")
