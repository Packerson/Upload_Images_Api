import uuid

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import filters, generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from datetime import datetime, timedelta
from django.http import HttpResponse

from .serializer import LinksSerializer
from .models import Links
from apps.images.models import Image
from .exceptions import ImageNotFound


class LinksAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):

        data = self.request.data
        time = data['time']
        id = data['id']
        try:
            image = Image.objects.get(id=id)
        except Image.DoesNotExist:
            raise ImageNotFound

        user = request.user
        if image.user != user:
            return Response(
                {"error": "You can't create link to image"
                          " that doesn't belong to you"},
                status=status.HTTP_403_FORBIDDEN,
            )
        if image.tier() == "BASIC" or image.tier() == "PREMIUM":
            return Response(
                {"error": "You are not allowed to create expiring links"},
                status=status.HTTP_403_FORBIDDEN,
            )
        uuid_link = uuid.uuid4()
        expiration_date = datetime.now() + timedelta(seconds=time)
        link = Links.objects.create(link=image.image,
                                    user=user,
                                    time=time,
                                    expiration_date=expiration_date,
                                    expiration_link=uuid_link)
        link.save()
        serializer = LinksSerializer(link, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UuidLinkViewAPIView(APIView):

    def get(self, request, uuid_link):
        print(uuid_link)
        try:
            link = Links.objects.get(expiration_link=uuid_link)
        except Links.DoesNotExist:
            raise ImageNotFound

        return Response(link.link, status=status.HTTP_200_OK)
