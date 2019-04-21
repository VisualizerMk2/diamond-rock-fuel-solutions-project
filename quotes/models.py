from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from users.models import CustomUser
from localflavor.us.models import USZipCodeField

# Create your models here.
User = settings.AUTH_USER_MODEL

class FuelQuote(models.Model):
    gallons_requested = models.PositiveIntegerField(blank=False)
    delivery_street = models.CharField(max_length=200)
    delivery_state = models.CharField(max_length=30, blank=False)
    delivery_zipcode = USZipCodeField()
    delivery_date = models.DateField(blank=False)
    total_amount_due = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
