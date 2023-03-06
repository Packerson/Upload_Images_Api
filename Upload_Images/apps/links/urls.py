from django.urls import path
from .views import LinksAPIView, UuidLinkViewAPIView


urlpatterns = [
    path('', LinksAPIView.as_view(), name="links"),
    path('<str:uuid_link>', UuidLinkViewAPIView.as_view(), name="links"),
]
