from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import filters, generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from datetime import datetime, timedelta

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

        print(data)
        expiration_date = datetime.now() + timedelta(seconds=time)
        print(image.image_url(), time, expiration_date)
        link = Links.objects.create(link=image.image, user=user, time=time, expiration_date=expiration_date)
        link.save()
        return Response("serializer.data")
