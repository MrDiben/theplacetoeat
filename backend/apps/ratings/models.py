from django.db import models
from django.utils.translation import gettext as _


class Rating(models.Model):
    restaurant = models.OneToOneField(
        "place.Restaurant",
        verbose_name=_("Restaurant"),
        on_delete=models.CASCADE,
        related_name="rating",
        unique=True,
    )
    google_rating_average = models.FloatField(blank=True, null=True)
    google_user_ratings_total = models.IntegerField(blank=True, null=True)
    user_ratings_total = models.IntegerField(blank=True, null=True)
    rating_average = models.FloatField(blank=True, null=True)


class Review(models.Model):
    """ Restaurant Reviews """

    restaurant = models.ForeignKey(
        "place.Restaurant",
        verbose_name=_("Restaurant"),
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    author = models.ForeignKey(
        "user.UserProfile",
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        related_name="reviews",
        blank=True,
        null=True,
    )
    author_name = models.CharField(max_length=30, blank=True, null=True)
    author_url = models.URLField(max_length=256, blank=True, null=True)
    profile_photo_url = models.URLField(max_length=200, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    relative_time_description = models.CharField(max_length=30, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ["restaurant", "author", "author_name", "created_at"]
