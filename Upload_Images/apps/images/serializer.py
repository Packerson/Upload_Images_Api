from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    email = serializers.EmailField(source="user.email")
    tier = serializers.CharField(source="user.profile.tier")

    class Meta:
        model = Image
        fields = [
            'username',
            'email',
            'id',
            'title',
            'date_creation',
            'alt',
            'tier',
            'image',
            'image_200',
            'image_400',
            ]


class UpdatedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['title',
                  'alt',
                  'image']
