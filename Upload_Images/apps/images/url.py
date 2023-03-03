from django.urls import path

from .models import Image
from .serializer import ImageSerializer
from .views import (ImageViewSet,
                    GetUsersImagesViewSet,
                    ImageUploadViewSet,
                    BasicPlanListApiView,
                    EnterprisePlanListApiView,
                    PremiumPlanListApiView,
                    )

urlpatterns = [
    path("all/", ImageViewSet.as_view(), name="images"),
    path("upload/", ImageUploadViewSet.as_view(), name="upload_image"),
    path("my/", GetUsersImagesViewSet.as_view(queryset=Image.objects.all(), serializer_class=ImageSerializer),
         name="user_images"),
    path("basic/", BasicPlanListApiView.as_view(queryset=Image.objects.all(), serializer_class=ImageSerializer),
         name="basic_images"),
    path("premium/", PremiumPlanListApiView.as_view(queryset=Image.objects.all(), serializer_class=ImageSerializer),
         name="premium_images"),
    path("enterprise/",
         EnterprisePlanListApiView.as_view(queryset=Image.objects.all(), serializer_class=ImageSerializer),
         name="enterprise_images"),
]
