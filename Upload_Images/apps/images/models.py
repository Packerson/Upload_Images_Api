from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_image_file_extension

from apps.profiles.models import Profile

User = get_user_model()


def user_directory_path(instance, filename):
    return 'images/{0}'.format(filename)


class Image(models.Model):
    user = models.ForeignKey(User, related_name="image",
                             on_delete=models.CASCADE)
    plan = models.ForeignKey(Profile, related_name="plan",
                             on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, unique=True)
    alt = models.TextField(null=True)
    date_creation = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to=user_directory_path)

    def __str__(self):
        return f"{self.user.username}'s image"
