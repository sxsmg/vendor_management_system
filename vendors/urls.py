from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet, VendorPerformanceView

router = DefaultRouter()
router.register(r'vendors', VendorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('vendors/<int:vendor_id>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
]