from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Custom(models.Model):

    """In admin panel, Admin can create a custom resolution. """

    resolution = models.IntegerField(default=0, unique=True)

    def __str__(self):
        return f"Height in px: {self.resolution}"


class Profile(models.Model):

    """Tiers for users """

    TIER = (
        ('BASIC', 'Basic'),
        ('PREMIUM', 'Premium'),
        ('ENTERPRISE', 'Enterprise'),
        ('CUSTOM', 'Custom')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    tier = models.CharField(max_length=10, choices=TIER, default='BASIC')
    custom_resolution = models.ForeignKey(Custom, on_delete=models.CASCADE, related_name="profile",
                                          null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} {self.tier} Profile'

    def save(self, **kwargs):
        if self.tier != "CUSTOM":
            self.custom_resolution = None

        super(Profile, self).save()
