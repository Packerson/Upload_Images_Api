from rest_framework import serializers
from .models import Profile, Custom


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    full_name = serializers.SerializerMethodField(read_only=True)
    resolution = serializers.CharField(source='custom_resolution.resolution', required=False)

    class Meta:
        model = Profile
        fields = [
            'username',
            'first_name',
            'last_name',
            'full_name',
            'email',
            'id',
            'tier',
            'resolution',
            'custom_resolution'
            ]
        extra_kwargs = {"resolution": {"required": False, "allow_null": True}}

    def get_full_name(self, obj):
        first_name = obj.user.first_name.title()
        last_name = obj.user.last_name.title()
        return f"{first_name} {last_name}"


class UpdatedProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            'tier',
            'custom_resolution'
        ]

    def update(self, instance, validated_data):
        instance.name = validated_data.get('tier', instance.tier)
        instance.save()
        return instance

