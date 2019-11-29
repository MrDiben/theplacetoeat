from datetime import date

from celery import shared_task
from recommendation.models import Recommendation
from place.models import Restaurant
from django.db import transaction
from place.utils import MATCHING_DAYS
import logging

logger = logging.getLogger(__name__)


@shared_task
@transaction.atomic
def set_recommendations(userprofile_id=None):
    from user.models import UserProfile

    if userprofile_id:
        logger.info(f"Set recommendations for user {userprofile_id}")
        queryset = UserProfile.objects.filter(pk=userprofile_id)
    else:
        logger.info("Set recommendations for users...")
        queryset = UserProfile.objects.all()
    for user_profile in queryset:
        #   Reset recommendations
        logger.info(f"Delete old recommendations for user {user_profile.pk}")
        user_profile.recommendations.all().delete()
        #    Get Weekday
        weekday = MATCHING_DAYS[date.today().weekday()]
        #   Get restaurant with openhours for week day
        restaurants = Restaurant.objects.filter(open_hours__week_day=weekday)
        #   Exclude restaurants with no photos (UI dept)
        exclude_no_photo = []
        for restaurant in restaurants:
            if restaurant.main_photo and restaurant.main_photo.url:
                continue
            photo = restaurant.photos.filter(url__isnull=False).first()
            if photo:
                continue
            exclude_no_photo.append(restaurant.pk)
        restaurants = restaurants.exclude(pk__in=exclude_no_photo).order_by("?")[
            :5
        ]  # Get 5 random restaurants with a photo

        #  Create new recommendations for the half day
        for restaurant in restaurants:
            recommendation, _created = Recommendation.objects.get_or_create(
                user_profile=user_profile, restaurant=restaurant
            )
            recommendation.current = True
            recommendation.save()
    logger.info("Set recommendations for users ended successfully")
    return f"Set recommendations for {len(queryset)} users"
