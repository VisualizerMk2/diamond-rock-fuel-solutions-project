from django.db import models

# Create your models here.
class FuelQuote(models.Model):
    gallons_requested = PositiveIntegerField()
    delivery_address = CharField(max_length=200)
    delivery_date = DateField()
    suggested_price = DecimalField(decimal_places=2)
    total_amount_due = DecimalField(decimal_places=2)