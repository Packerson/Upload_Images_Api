from rest_framework import serializers
from .models import Links
from ..images.models import Image


class LinksSerializer(serializers.ModelSerializer):

    user = serializers.CharField(source="image.user.username")

    class Meta:
        model = Links
        fields = [
            'user',
            'image',
            'time',
            'expiration_date',
            'expiration_link',
            'get_expiration_link'
        ]


class GenerateLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ['image']

