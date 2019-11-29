from datetime import datetime
from rest_framework import serializers

from meal.models import Meal, InvitationMeal
from user.serializers import UserProfileSerializer
from place.serializers import LightRestaurantSerializer


class MealSerializer(serializers.ModelSerializer):
    creator = UserProfileSerializer(many=False, read_only=True)
    restaurant = LightRestaurantSerializer(many=False, read_only=True)
    closed = serializers.SerializerMethodField()

    class Meta:
        model = Meal
        fields = ("creator", "datehour", "restaurant", "closed")

    def get_closed(self, meal):
        return not meal.datehour.date() == datetime.today().date()


class InvitationMealSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(many=False, read_only=True)
    meal = MealSerializer(many=False, read_only=True)
    is_creator = serializers.SerializerMethodField()

    class Meta:
        model = InvitationMeal
        fields = ("pk", "user", "meal", "status", "note", "is_creator")

    def get_is_creator(self, invitation_meal):
        return invitation_meal.meal.creator == invitation_meal.user
