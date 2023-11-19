from django.db import models
from django.db.models import F, Avg, Case, When, IntegerField, Sum


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=100, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

    def calculate_on_time_delivery_rate(self):
        total_orders = self.purchase_orders.count()
        on_time_orders = self.purchase_orders.filter(delivery_date__lte=F('order_date')).count()
        return (on_time_orders / total_orders) * 100 if total_orders > 0 else 0

    def calculate_quality_rating_avg(self):
        return self.purchase_orders.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0

    def calculate_average_response_time(self):
        total_response_time = self.purchase_orders.annotate(
            response_time=Case(
                When(acknowledgment_date__isnull=False, then=F('acknowledgment_date') - F('issue_date')),
                default=0,
                output_field=IntegerField()
            )
        ).aggregate(total=Sum('response_time'))['total']

        total_responses = self.purchase_orders.filter(acknowledgment_date__isnull=False).count()
        return total_response_time / total_responses if total_responses > 0 else 0

    def calculate_fulfillment_rate(self):
        total_orders = self.purchase_orders.count()
        fulfilled_orders = self.purchase_orders.filter(status="Fulfilled").count()
        return (fulfilled_orders / total_orders) * 100 if total_orders > 0 else 0