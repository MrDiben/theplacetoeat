from datetime import date
from rest_framework import serializers

from place.models import Restaurant, CookType, OpenHour
from photos.serializers import PhotoSerializer
from ratings.serializers import RatingSerializer
from place.utils import MATCHING_DAYS
from location.serializers import CitySerializer


class CookTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookType
        fields = ("name",)


class OpenHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenHour
        fields = "__all__"


class LightRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("name", "google_map_url", "formatted_address")
        model = Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    city = CitySerializer(many=False, read_only=True)
    photo_header = serializers.SerializerMethodField(read_only=True)
    cook_types = CookTypeSerializer(many=True, read_only=True)
    rating = RatingSerializer(many=False, read_only=True)
    today_hours = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Restaurant
        fields = "__all__"

    def get_photo_header(self, restaurant):
        if restaurant.main_photo and restaurant.main_photo.url:
            return restaurant.main_photo.url
        photo = restaurant.photos.filter(url__isnull=False).first()
        if photo:
            return photo.url
        return None

    def get_today_hours(self, restaurant):
        weekday = MATCHING_DAYS[date.today().weekday()]
        return [
            OpenHoursSerializer(oh).data
            for oh in restaurant.open_hours.filter(week_day=weekday)
        ]
