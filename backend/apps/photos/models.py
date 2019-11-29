from django.db import models
from django.utils.translation import gettext as _


class Photo(models.Model):
    restaurant = models.ForeignKey(
        "place.Restaurant",
        verbose_name=_("Restaurant"),
        on_delete=models.CASCADE,
        related_name="photos",
        blank=True,
        null=True,
    )
    filename = models.CharField(max_length=100, verbose_name=_("Week Day"))
    width = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    url = models.URLField(max_length=256, blank=True, null=True, unique=True)
    google_photo_reference = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        unique=True,
        verbose_name=_("Google Photo Reference"),
    )
