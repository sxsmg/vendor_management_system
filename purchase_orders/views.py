from rest_framework import viewsets
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .models import PurchaseOrder

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderAcknowledgeView(APIView):
    def post(self, request, po_id):
        purchase_order = get_object_or_404(PurchaseOrder, pk=po_id)
        purchase_order.acknowledgment_date = datetime.now()
        purchase_order.save()

        # Optionally, you can recalculate average response time here or use signals

        return Response(status=status.HTTP_204_NO_CONTENT)