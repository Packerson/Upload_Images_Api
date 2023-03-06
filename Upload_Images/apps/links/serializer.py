from rest_framework import serializers
from .models import Links


class LinksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Links
        fields = [
            'user',
            'link',
            'expiration_date',
            'expiration_link',
            'get_expiration_link'
        ]


