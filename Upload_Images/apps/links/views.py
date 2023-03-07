import uuid

from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from datetime import datetime, timedelta


from .serializer import LinksSerializer, GenerateLinkSerializer
from .models import Links
from apps.images.models import Image
from .exceptions import ImageNotFound, LinkExpiredError


class LinksAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    """
    Class for generated unique link only for permission user
    """
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

        """Check if use is allowed to generate expiration link"""
        if image.tier() == "BASIC" or image.tier() == "PREMIUM":
            return Response(
                {"error": "You are not allowed to create expiring links"},
                status=status.HTTP_403_FORBIDDEN,
            )

        """Create unique id and transfer it as link"""
        uuid_link = uuid.uuid4()
        expiration_date = datetime.now() + timedelta(seconds=time)
        link = Links.objects.create(image=image,
                                    time=time,
                                    expiration_date=expiration_date,
                                    expiration_link=uuid_link)
        link.save()
        serializer = LinksSerializer(link, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)


class UuidLinkViewAPIView(APIView):

    """
        Check if link exists,
        Check if link is expired:
            yes -> link is deleted,
            no  -> get link to image
            """
    def get(self, request, uuid_link):

        try:
            link = Links.objects.get(expiration_link=uuid_link)
        except Links.DoesNotExist:
            raise ImageNotFound

        if link.expiration_date < datetime.now():
            link.delete()
            raise LinkExpiredError

        serializer = GenerateLinkSerializer(link.image, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
