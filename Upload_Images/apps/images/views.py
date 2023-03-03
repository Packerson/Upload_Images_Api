from django.http import HttpResponse
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import generics, permissions, status, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.utils import json
from rest_framework.views import APIView

from .models import Image
from .renderers import ImageJSONRenderer
from .serializer import ImageSerializer


class ImageViewSet(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageUploadViewSet(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        file = request.data['file']

        if file.name.lower().endswith('.jpg') or file.name.lower().endswith('.png'):

            print(file)
            title = request.data['title']
            alt = request.data['alt']

            user = self.request.user
            image = Image.objects.create(image=file, user=user, title=title, alt=alt)
            serializer = ImageSerializer(image)
            print(image)
            return Response(serializer.data, status=status.HTTP_200_OK)
        raise ValidationError('Wrong extension, only jpg and png are accepted ')


class GetUsersImagesViewSet(generics.ListAPIView):
    """Generic Users Images"""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = [ImageSerializer]

    def get_queryset(self):
        user = self.request.user
        return Image.objects.filter(user=user)


class BasicPlanListApiView(generics.ListAPIView):
    """Generic list of BasicPlan"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Image.objects.filter(user__profile__tier="BASIC")


class PremiumPlanListApiView(generics.ListAPIView):
    """Generic list of PremiumPlan"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Image.objects.filter(user__profile__tier="PREMIUM")


class EnterprisePlanListApiView(generics.ListAPIView):
    """Generic list of EnterprisePlan"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Image.objects.filter(user__profile__tier="ENTERPRISE")


class CustomPlanListApiView(generics.ListAPIView):
    """Generic list of EnterprisePlan"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Image.objects.filter(user__profile__tier="CUSTOM")
#

