from django.shortcuts import render
from rest_framework import viewsets
from .models import Vendor
from .serializers import VendorSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorPerformanceView(APIView):
    def get(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
        except Vendor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        performance_data = {
            'on_time_delivery_rate': vendor.calculate_on_time_delivery_rate(),
            'quality_rating_avg': vendor.calculate_quality_rating_avg(),
            'average_response_time': vendor.calculate_average_response_time(),
            'fulfillment_rate': vendor.calculate_fulfillment_rate()
        }
        return Response(performance_data)