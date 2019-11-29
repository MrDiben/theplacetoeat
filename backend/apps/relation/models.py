from django.db import models
from django.utils.translation import gettext as _


class FriendShip(models.Model):
    user_1 = models.ForeignKey(
        "user.UserProfile",
        verbose_name=_("User Sending Invitation"),
        on_delete=models.CASCADE,
        related_name="creator_friendships",
    )
    user_2 = models.ForeignKey(
        "user.UserProfile",
        verbose_name=_("User Receiving Invitation"),
        on_delete=models.CASCADE,
        related_name="invited_friendships",
    )
    status = models.BooleanField(default=False, verbose_name=_("Is Accepted ?"))

    class Meta:
        unique_together = ["user_1", "user_2"]
