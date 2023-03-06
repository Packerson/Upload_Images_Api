from django.urls import path

from .views import (BasicPlanListApiView,
                    PremiumPlanListApiView,
                    EnterprisePlanListApiView,
                    UpdateProfileApiView,
                    GetProfileApiView)

urlpatterns = [
    path("me/", GetProfileApiView.as_view(), name="get_profile"),
    path("update/<str:username>/", UpdateProfileApiView.as_view(), name="update_profile"),
    path("plan/basic/", BasicPlanListApiView.as_view(), name="basic_plan"),
    path("plan/premium/", PremiumPlanListApiView.as_view(), name="premium_plan"),
    path("plan/enterprise/", EnterprisePlanListApiView.as_view(), name="enterprise_plan"),
    ]


"""also should be other plans creating by admin"""

