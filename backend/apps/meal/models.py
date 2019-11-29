from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MinValueValidator, MaxValueValidator


class Meal(models.Model):
    creator = models.ForeignKey(
        "user.UserProfile",
        verbose_name=_("Meal creator"),
        on_delete=models.CASCADE,
        related_name="my_created_meals",
    )
    datehour = models.DateTimeField(verbose_name=_("Meal Date Hour"))
    restaurant = models.ForeignKey(
        "place.Restaurant",
        verbose_name=_("Meal Restaurant"),
        on_delete=models.CASCADE,
        related_name="organised_meals",
    )

    class Meta:
        unique_together = ["datehour", "creator"]


class InvitationMeal(models.Model):
    meal = models.ForeignKey(
        Meal, verbose_name=_("Meal"), on_delete=models.CASCADE, related_name="invitations"
    )
    user = models.ForeignKey(
        "user.UserProfile",
        verbose_name=_("Invited Meal User"),
        on_delete=models.CASCADE,
        related_name="my_meals",
    )
    status = models.BooleanField(default=False, verbose_name=_("Is Accepted ?"))
    note = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(10), MinValueValidator(0)],
        verbose_name=_("User Note"),
    )

    class Meta:
        unique_together = ["meal", "user"]
