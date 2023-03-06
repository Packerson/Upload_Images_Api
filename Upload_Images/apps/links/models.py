from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

User = get_user_model()

"""
Foregin key to Image, not to user , will be easier to return a image"""


class Links(models.Model):
    user = models.ForeignKey(User,
                             related_name="link_user",
                             on_delete=models.CASCADE)

    link = models.CharField(max_length=255)

    time = models.IntegerField(default=300,
                               help_text="Seconds",
                               validators=[MinValueValidator(300), MaxValueValidator(30000)])

    date_creation = models.DateTimeField(default=timezone.now, editable=False)
    expiration_date = models.DateTimeField(null=True)
    expiration_link = models.CharField(null=True, max_length=200)

    def __str__(self):
        return f"Expiring link belong to {self.user.username} time in seconds {self.time}"

    def get_expiration_link(self):
        return f"/api-auth/links/{self.expiration_link}"
    class Meta:
        verbose_name_plural = "Links"
