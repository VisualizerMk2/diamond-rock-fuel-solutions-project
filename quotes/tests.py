from django.test import TestCase
from django.test import Client
from .forms import *   # import all forms
from users.forms import *
import datetime



# Create your tests here.
class Setup_Class(TestCase):
  def setUp(self):
    self.user = CustomUser.objects.create(
      username='test_user',
      full_name='John Doe',
      company_name='test company',
      address1='123 Test Lane',
      address2='Suite 101',
      city='Houston',
    )

class TestQuoteForm(TestCase):
  def setUp(self):
    self.user = CustomUser.objects.create(
      username='test_user',
      full_name='John Doe',
      company_name='test company',
      address1='123 Test Lane',
      address2='Suite 101',
      city='Houston',
    )

  def test_QuoteForm_valid(self):
    user_pk = CustomUser.objects.get(pk=1).pk
    form = FuelQuoteModelForm(data={
      'user': user_pk,
      'delivery_date': "2019-06-10",
      'gallons_requested': 100,
      'delivery_state': "Texas",
      'delivery_street': "1234 Test Lane",
      'delivery_zipcode':"77002"})
    self.assertTrue(form.is_valid())

  def test_UserForm_invalid(self):
    form = CustomUserCreationForm(data={'username':"",
      'full_name':"",
      'company_name':"",
      'address1':"",
      'address2':"",
      'city':""})
    self.assertFalse(form.is_valid())

# class FuelQuoteCreationTest(TestCase):
#   def test_
