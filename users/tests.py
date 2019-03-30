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

class UserFormsTest(TestCase):
    form = CustomUserChangeForm()
    
    def test_form_placeholders(self):
      self.assertEqual(self.form.fields['address1'].widget.attrs['placeholder'], 'Address 1')
      self.assertEqual(self.form.fields['address1'].label, '')
      self.assertEqual(self.form.fields['address2'].widget.attrs['placeholder'], 'Address 2')
      self.assertEqual(self.form.fields['address2'].label, '')
      self.assertEqual(self.form.fields['city'].widget.attrs['placeholder'], 'City')
      self.assertEqual(self.form.fields['city'].label, '')
      self.assertEqual(self.form.fields['zipcode'].widget.attrs['placeholder'], 'Zipcode')
      self.assertEqual(self.form.fields['zipcode'].label, '')
      self.assertEqual(self.form.fields['state'].widget.attrs['placeholder'], 'State')
      self.assertEqual(self.form.fields['state'].label, '')
