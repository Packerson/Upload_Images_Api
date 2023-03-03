from django.http import HttpResponse
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
        print(file)
        title = request.data['title']
        alt = request.data['alt']

        user = self.request.user
        image = Image.objects.create(image=file, user=user, title=title, alt=alt, plan=user.profile)
        serializer = ImageSerializer(image)
        print(image)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
        return Image.objects.filter(plan__is_basic=True)


class PremiumPlanListApiView(generics.ListAPIView):
    """Generic list of PremiumPlan"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Image.objects.filter(plan__is_premium=True)


class EnterprisePlanListApiView(generics.ListAPIView):
    """Generic list of EnterprisePlan"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Image.objects.filter(plan__is_enterprise=True)
#
#
# class PremiumPlanListApiView(generics.ListAPIView):
#     """Generic list of PremiumPlan"""
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Image.objects.filter(is_premium=True)
#     serializer_class = ImageSerializer
#
#
# class EnterprisePlanListApiView(generics.ListAPIView):
#     """Generic list of EnterprisePlan"""
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Image.objects.filter(is_enterprise=True)
#     serializer_class = ImageSerializer
