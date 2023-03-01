from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile",
                                on_delete=models.CASCADE)
    is_basic = models.BooleanField(verbose_name=_("Basic"), default=False,
                                   help_text=_("Basic plan?"))
    is_premium = models.BooleanField(verbose_name=_("Premium"), default=False,
                                     help_text=_("Premium plan?"))
    is_enterprise = models.BooleanField(verbose_name=_("Enterprise"), default=False,
                                        help_text=_("Enterprise plan?"))

    def __str__(self):
        return f"{self.user.username}'s profile "
