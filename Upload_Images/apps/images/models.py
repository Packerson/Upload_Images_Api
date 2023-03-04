from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_image_file_extension
from rest_framework.exceptions import ValidationError
from django_resized import ResizedImageField
from apps.profiles.models import Profile
from PIL import Image as PIL_IMAGE
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from io import BytesIO

User = get_user_model()


def user_directory_path(instance, filename):
    return 'images/{0}'.format(filename)


def user_directory_path_200(instance, filename):
    return 'images_200/{0}'.format(filename)


def user_directory_path_400(instance, filename):
    return 'images_400/{0}'.format(filename)


def user_directory_path_custom(instance, filename):
    return 'images_custom/{0}'.format(filename)


class Image(models.Model):
    user = models.ForeignKey(User, related_name="user",
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    alt = models.TextField(null=True)
    date_creation = models.DateTimeField(default=timezone.now)
    """extension validation in views method"""
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    image_200 = models.ImageField(upload_to=user_directory_path_200, null=True, blank=True)
    image_400 = models.ImageField(upload_to=user_directory_path_400, null=True, blank=True)
    image_custom = models.ImageField(upload_to=user_directory_path_custom, null=True, blank=True)

    def save(self, **kwargs):


        # print(self.user.profile.custom_resolution.resolution)

        if self.user.profile.tier != "CUSTOM":

            """Creating thumbnail 200px"""

            output_size_200 = (200, 200)
            output_thumb_200 = BytesIO()

            img_200 = PIL_IMAGE.open(self.image)

            img_name = self.image.name.split('.')[0]

            if img_200.height != 200 or img_200.width != 200:
                img_200.thumbnail(output_size_200)
                img_200.save(output_thumb_200, format='JPEG', quality=90)

            self.image_200 = InMemoryUploadedFile(output_thumb_200, 'ImageField', f"{img_name}_thumb_200.jpg",
                                                  'image/jpg',
                                                  sys.getsizeof(output_thumb_200), None)

            if self.user.profile.tier == "PREMIUM" or self.user.profile.tier == "ENTERPRISE":
                """Creating thumbnail 400px"""

                output_size_400 = (400, 400)
                output_thumb_400 = BytesIO()

                img_400 = PIL_IMAGE.open(self.image)

                if img_400.height != 400 or img_400.width != 400:
                    img_400.thumbnail(output_size_400)
                    img_400.save(output_thumb_400, format='JPEG', quality=90)

                self.image_400 = InMemoryUploadedFile(output_thumb_400, 'ImageField', f"{img_name}_thumb_400.jpg",
                                                      'image/jpg',
                                                      sys.getsizeof(output_thumb_400), None)

        if self.user.profile.tier == "CUSTOM":
            size = int(self.user.profile.custom_resolution.resolution)

            """Creating thumbnail Custom PX"""

            output_size_custom = (size, size)
            output_thumb_custom = BytesIO()

            img_custom = PIL_IMAGE.open(self.image)
            img_name = self.image.name.split('.')[0]

            img_custom.thumbnail(output_size_custom)
            img_custom.save(output_thumb_custom, format='JPEG', quality=90)

            self.image_custom = InMemoryUploadedFile(output_thumb_custom,
                                                     'ImageField', f"{img_name}_thumb_custom.jpg",
                                                     'image/jpg',
                                                     sys.getsizeof(output_thumb_custom), None)

        if self.user.profile.tier == "BASIC":
            """Only basic tier can't have original size"""
            self.image = None

        super(Image, self).save()

    def __str__(self):
        return f"{self.user.username}'s image"

    def tier(self):
        return f"{self.user.profile.tier}"
