from django.conf import settings
from django.db import models, transaction
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext as _

from place.models import Restaurant


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        related_name="user_profile",
        blank=True,
        null=True,
    )
    city = models.ForeignKey(
        "location.City",
        verbose_name=_("City"),
        on_delete=models.CASCADE,
        related_name="users",
        blank=True,
        null=True,
    )
    restaurants = models.ManyToManyField(
        "place.Restaurant", through="recommendation.Recommendation"
    )

    def __str__(self):
        if self.user:
            if self.user.first_name and self.user.last_name:
                return f"{self.user.first_name} {self.user.last_name}"
            return f"{self.user.username} {self.user.email}"

    def get_restaurants(self):
        #   Default to Villeurbanne / Lyon for now:
        return Restaurant.objects.filter(city__name__in=["Villeurbanne", "Lyon"])


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create(sender, instance, created, **kwargs):

    if created:
        UserProfile.objects.update_or_create(user=instance)


@receiver(post_save, sender=UserProfile)
def create_recommendations(sender, instance, created, **kwargs):
    if created:
        from recommendation.tasks import set_recommendations

        #  Set recommendations
        transaction.on_commit(lambda: set_recommendations.delay(userprofile_id=instance.pk))
