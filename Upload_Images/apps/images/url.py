from django.urls import path


from .views import (ImageViewSet,
                    GetUsersImagesViewSet,
                    )

urlpatterns = [
    path("all/", ImageViewSet.as_view(), name="images"),
    path("my/", GetUsersImagesViewSet.as_view(), name="user_images"),
]
