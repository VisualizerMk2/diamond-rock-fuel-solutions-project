from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from crispy_forms.helper import FormHelper
from localflavor.us.models import USStateField, USZipCodeField


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = [
            'username',
            'full_name',
            'email',
            'password1',
            'password2'
        ]

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs['placeholder'] = field.label
            field.label = ''
            field.help_text = ''


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = [
            'company_name',
            'full_name',
            'email',
            'address1',
            'address2',
            'city',
            'zipcode',
            'password',
            'state',
        ]

    def clean_zipcode(self):
        zipcode = self.cleaned_data['zipcode']
        if len(zipcode) < 5:
            raise ValidationError("Zipcode must be 5 digits long")
        return zipcode


    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field= self.fields.get(field_name)
            field.widget.attrs['placeholder'] = field.label
            field.label= ''
        # self.fields['full_name'].widget.attrs['placeholder'] = 'Full Name'
        # self.fields['full_name'].label = ''
        # self.fields['company_name'].widget.attrs['placeholder'] = 'Company Name'
        # self.fields['company_name'].label = ''
        # self.fields['address1'].widget.attrs['placeholder'] = 'Address 1'
        # self.fields['address1'].label = ''
        # self.fields['address2'].widget.attrs['placeholder'] = 'Address 2'
        # self.fields['address2'].label = ''
        # self.fields['city'].widget.attrs['placeholder'] = 'City'
        # self.fields['city'].label = ''
        # self.fields['zipcode'].widget.attrs['placeholder'] = 'Zipcode'
        # self.fields['zipcode'].label = ''
        # self.fields['state'].widget.attrs['placeholder'] = 'State'
        # self.fields['state'].label = ''


class UserLoginForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'password'
        ]

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs['placeholder'] = field.label
            field.label = ''
            field.help_text = ''
