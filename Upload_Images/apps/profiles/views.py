from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from .renderers import ProfileJSONRenderer
from .serializers import ProfileSerializer, UpdatedProfileSerializer


class BasicPlanListApiView(generics.ListAPIView):
    """Generic list of BasicPlan"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.filter(tier="BASIC")
    serializer_class = ProfileSerializer


class PremiumPlanListApiView(generics.ListAPIView):
    """Generic list of PremiumPlan"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.filter(tier="PREMIUM")
    serializer_class = ProfileSerializer


class EnterprisePlanListApiView(generics.ListAPIView):
    """Generic list of EnterprisePlan"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.filter(tier="ENTERPRISE")
    serializer_class = ProfileSerializer


class GetProfileApiView(APIView):
    """Generic profile View"""
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]

    def get(self, request):
        user = self.request.user
        user_profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(user_profile, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)



