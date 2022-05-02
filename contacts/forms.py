from django import forms
from django.forms import ModelForm, TextInput, EmailInput, ImageField
from django_countries.fields import CountryField

from .models import Contact

class DateInput(forms.DateInput):
    input_type = 'date'



class ContactForm(forms.ModelForm):
    class Meta:
      model=Contact
      fields="__all__"

      widgets = {
            'date_of_birth': DateInput()
        }

      # widgets = {

      #   'img': ImageField(attrs={
      #           'class': "form-control",
      #           'style': 'm ax-width: 300px;',
      #           'placeholder': 'Name'
      #           }),
      #   'f_name': TextInput(attrs={
      #           'class': "form-control",
      #           'style': 'm ax-width: 300px;',
      #           'placeholder': 'f_name'
      #           }),

      #   'l_name': TextInput(attrs={
      #           'class': "form-control",
      #           'style': 'm ax-width: 300px;',
      #           'placeholder': 'l_name'
      #           }),
      #   'email': EmailInput(attrs={
      #           'class': "form-control",
      #           'style': 'm ax-width: 300px;',
      #           'placeholder': 'Name'
      #           }),
      #   'gender': TextInput(attrs={
      #           'class': "form-control",
      #           'style': 'm ax-width: 300px;',
      #           'placeholder': 'gender'
      #           }),
      #   'per_address': TextInput(attrs={
      #           'class': "form-control",
      #           'style': 'm ax-width: 300px;',
      #           'placeholder': 'per_address'
      #           }),
      #   'pr_country': CountryField(attrs={
      #           'class': "form-control",
      #           'style': 'm ax-width: 300px;',
      #           'placeholder': 'pr_country'
      #           }),
      #   'cor_address': TextInput(attrs={
      #           'class': "form-control",
      #           'style': 'm ax-width: 300px;',
      #           'placeholder': 'cor_address'
      #           }),
      #   'cr_country': TextInput(attrs={
      #           'class': "form-control",
      #           'style': 'm ax-width: 300px;',
      #           'placeholder': 'Name'
      #           }),
      #   'tax_id': TextInput(attrs={
      #           'class': "form-control",
      #           'style': 'm ax-width: 300px;',
      #           'placeholder': 'Name'
      #           }),
      #   'f_name': TextInput(attrs={
      #           'class': "form-control",
      #           'style': 'm ax-width: 300px;',
      #           'placeholder': 'Name'
      #           }),
      #   'f_name': TextInput(attrs={
      #           'class': "form-control",
      #           'style': 'm ax-width: 300px;',
      #           'placeholder': 'Name'
      #           }),
      #   'f_name': TextInput(attrs={
      #           'class': "form-control",
      #           'style': 'm ax-width: 300px;',
      #           'placeholder': 'Name'
      #           }),
              
      # }