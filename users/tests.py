from django.test import TestCase, SimpleTestCase
from .models import CustomUser
from django.urls import reverse
from .forms import CustomUserChangeForm
# Create your tests here.


class UserModelCreationlTest(TestCase):
  
  def setUp(self):
    CustomUser.objects.create(
      username='test_user',
      full_name='John Doe',
      company_name='test company',
      address1='123 Test Lane',
      address2='Suite 101',
      city='Houston',
    )
  
  def test_user_fields(self):
    user = CustomUser.objects.get(id=1)
    expected_user_name = f'{user.username}'
    expected_full_name = f'{user.full_name}'
    expected_company_name = f'{user.company_name}'
    expected_address1 = f'{user.address1}'
    expected_address2 = f'{user.address2}'
    expected_city = f'{user.city}'
    self.assertEqual(expected_user_name, 'test_user')
    self.assertEqual(expected_company_name, 'test company')
    self.assertEqual(expected_full_name, 'John Doe')
    self.assertEqual(expected_address1, '123 Test Lane')
    self.assertEqual(expected_address2, 'Suite 101')
    self.assertEqual(expected_city, 'Houston')