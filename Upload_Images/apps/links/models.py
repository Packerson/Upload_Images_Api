from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db import models
from .exceptions import TimeValueError

from apps.images.models import Image

User = get_user_model()


class Links(models.Model):
    image = models.ForeignKey(Image,
                              related_name="link_image",
                              on_delete=models.CASCADE,
                              editable=False,
                              null=True,
                              blank=True)

    time = models.IntegerField(default=300,
                               help_text="Seconds")

    date_creation = models.DateTimeField(default=timezone.now, editable=False)
    expiration_date = models.DateTimeField(null=True)
    expiration_link = models.CharField(null=True, max_length=200)

    def __str__(self):
        return f"Expiring link belong to {self.image.user.username}" \
               f" time in seconds {self.time}"

    def get_expiration_link(self):

        """Get full link to image"""
        return f"/api-auth/links/{self.expiration_link}"

    def clean(self):

        """Validata time range"""
        if self.time not in range(300, 30001):
            raise TimeValueError
        return self.time

    def save(self, **kwargs):

        """need to call validator"""
        self.clean()
        super(Links, self).save()

    class Meta:
        verbose_name_plural = "Links"
