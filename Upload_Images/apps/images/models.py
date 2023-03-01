from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_image_file_extension
User = get_user_model()


class Image(models.Model):
    user = models.OneToOneField(User, related_name="image",
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    # image = models.ImageField('Image', validators=[validate_image_file_extension()])
    image = models.ImageField('Image')
