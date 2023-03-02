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

    # def post(self, request, *args, **kwargs):
    #     file = request.data['file']
    #     image = Image.objects.create(image=file)
    #     return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)


class GetUsersImagesViewSet(APIView):
    """Generic Users Images"""
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ImageJSONRenderer]

    def get(self, request):
        user = self.request.user
        user_images = Image.objects.filter(user=user)
        images_array = []

        print(user_images)
        for image in user_images:
            images_array.append(image)


        print(images_array)

        # return HttpResponse("Hello")
        serializer = ImageSerializer(user_images, many=True, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)




# class BasicPlanListApiView(generics.ListAPIView):
#     """Generic list of BasicPlan"""
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Image.objects.filter(plan=)
#     serializer_class = ImageSerializer
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
