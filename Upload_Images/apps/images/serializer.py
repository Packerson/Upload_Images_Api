from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    email = serializers.EmailField(source="user.email")
    # basic = serializers.CharField(source='plan.is_basic')
    # premium = serializers.CharField(source='image.plan.is_premium')
    # enterprise = serializers.CharField(source='plan.is_enterprise')

    class Meta:
        model = Image
        depth = 1
        fields = [
            'username',
            'email',
            'id',
            'title',
            'date_creation',
            'alt',
            # 'basic',
            # 'premium',
            # 'enterprise',
            'plan',
            'image', ]


class UpdatedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['title',
                  'alt',
                  'image']
