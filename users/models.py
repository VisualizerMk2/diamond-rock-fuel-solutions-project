from django.db import models
from django.contrib.auth.models import AbstractUser
from localflavor.us.models import USStateField, USZipCodeField
# Create your models here.


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=50, blank=False)
    company_name = models.CharField(max_length=100, null=True)
    address1 = models.CharField(max_length=100, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, null=True)
    zipcode = USZipCodeField(null=True)
    state = USStateField(null=True)
