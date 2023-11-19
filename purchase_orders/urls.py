from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PurchaseOrderViewSet, PurchaseOrderAcknowledgeView

router = DefaultRouter()
router.register(r'purchase_orders', PurchaseOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('purchase_orders/<int:po_id>/acknowledge/', PurchaseOrderAcknowledgeView.as_view(), name='purchase-order-acknowledge'),
]
