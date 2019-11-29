from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MinValueValidator, MaxValueValidator


class Recommendation(models.Model):
    user_profile = models.ForeignKey(
        "user.UserProfile",
        verbose_name=_("Recommendation"),
        on_delete=models.CASCADE,
        related_name="recommendations",
        blank=True,
        null=True,
    )
    restaurant = models.ForeignKey(
        "place.Restaurant",
        verbose_name=_("Restaurant"),
        on_delete=models.CASCADE,
        related_name="recommendations",
        blank=True,
        null=True,
    )
    last_time_update = models.DateTimeField(auto_now=True, verbose_name=_("Last time update"))
    last_time_user_eat_in = models.DateField(
        null=True, blank=True, verbose_name=_("Last time user eat in")
    )
    score = models.PositiveSmallIntegerField(
        default=5,
        validators=[MaxValueValidator(10), MinValueValidator(0)],
        verbose_name=_("Recommendation Score"),
    )
    current = models.BooleanField(default=False, verbose_name=_("is current recommendation ?"))

    class Meta:
        unique_together = ["user_profile", "restaurant"]
