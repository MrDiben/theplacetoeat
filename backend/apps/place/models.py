from django.db import models
from django.utils.translation import gettext as _


class OpenHour(models.Model):
    restaurant = models.ForeignKey(
        "place.Restaurant",
        verbose_name=_("Restaurant"),
        on_delete=models.CASCADE,
        related_name="open_hours",
        blank=True,
        null=True,
    )
    week_day = models.CharField(max_length=15, verbose_name=_("Week Day"))
    open_hour = models.TimeField(_("Open Hour"), blank=True)
    close_hour = models.TimeField(_("Close Hour"), blank=True)

    class Meta:
        unique_together = ["restaurant", "week_day", "open_hour", "close_hour"]


class CookType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    city = models.ForeignKey(
        "location.City",
        verbose_name=_("City"),
        on_delete=models.CASCADE,
        related_name="restaurants",
        blank=True,
        null=True,
    )
    main_photo = models.ForeignKey(
        "photos.Photo",
        verbose_name=_("Main Photo"),
        on_delete=models.CASCADE,
        related_name="restaurants",
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=75, verbose_name=_("Restaurant Name"))
    description = models.TextField(
        null=True, blank=True, verbose_name=_("Restaurant Description")
    )
    price_indicator = models.CharField(
        max_length=3,
        choices=[("€€€", "€€€"), ("€€", "€€"), ("€", "€")],
        verbose_name=_("Price Indicator"),
        default="€€",
    )
    cook_types = models.ManyToManyField(
        CookType, related_name="restaurants", verbose_name=_("Cook Types")
    )
    website = models.URLField(
        max_length=256, unique=True, null=True, blank=True, verbose_name=_("Website")
    )
    is_active = models.BooleanField(default=False, verbose_name=_("Is Active ?"))
    from_google = models.BooleanField(default=False, verbose_name=_("Place from Google"))
    latitude = models.FloatField(blank=True, null=True, verbose_name=_("Latitude"))
    longitude = models.FloatField(blank=True, null=True, verbose_name=_("Longitude"))
    formatted_address = models.CharField(
        max_length=256, null=True, blank=True, verbose_name=_("Formatted address")
    )
    phone_number = models.CharField(
        max_length=20, null=True, blank=True, verbose_name=_("Phone Number")
    )
    google_place_id = models.CharField(
        max_length=256, unique=True, null=True, blank=True, verbose_name=_("Google Place Id")
    )
    google_map_url = models.URLField(
        max_length=256, null=True, unique=True, blank=True, verbose_name=_("Google Map URL")
    )

    def __str__(self):
        return self.name
