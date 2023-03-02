from django.urls import path

from .views import (ImageViewSet,
                    GetUsersImagesViewSet,
                    ImageUploadViewSet
                    )

urlpatterns = [
    path("all/", ImageViewSet.as_view(), name="images"),
    path("upload/", ImageUploadViewSet.as_view(), name="upload_image"),
    path("my/", GetUsersImagesViewSet.as_view(), name="user_images"),
]
