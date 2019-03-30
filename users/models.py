from django.db import models
from django.contrib.auth.models import AbstractUser
from localflavor.us.models import USStateField,USZipCodeField
# Create your models here.

class CustomUser(AbstractUser):
  full_name = models.CharField(max_length=50, blank=True, null=True)
  company_name = models.CharField(max_length=100, blank=True, null=True)
  address1 = models.CharField(max_length=100,blank=True, null=True)
  address2 = models.CharField(max_length=100,blank=True, null=True)
  city = models.CharField(max_length=100,blank=True, null=True)
  zipcode = USZipCodeField(null=True, blank=True)
  state = USStateField(null=True,blank=True )