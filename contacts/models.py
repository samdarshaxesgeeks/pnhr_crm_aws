from contextlib import nullcontext
from secrets import choice
from xmlrpc.client import Boolean
from django.db import models
from django_countries.fields import CountryField
from django.core.validators import RegexValidator
from imagefield.fields import ImageField
from datetime import date
# Create your models here.


SO_DO_CHOICE = (
    ('Son Of' , 'S/O'),
    ('Doughter Of' , 'D/O'),
)

BOOLEB = (
    ('True', 'T'),
    ('False', 'F'),
)

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


class Contact(models.Model):
    img = ImageField(upload_to='contact/', auto_add_fields=True, blank=True)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    gender = models.CharField(max_length=20)
    per_address = models.CharField(max_length=250)
    pr_country = CountryField()
    cor_address = models.CharField(max_length=250)
    cr_country = CountryField()
    tax_id = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    Age = models.IntegerField()
    high_education = models.CharField(max_length=250)
    occupation = models.CharField(max_length=150)
    no_of_experience = models.IntegerField()
    parent_f_name = models.CharField(max_length=50)
    parent_l_name = models.CharField(max_length=50)
    pas_no = models.CharField(max_length=16)
    pas_country = CountryField()
    telephone = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    telephone = models.CharField(validators=[telephone], max_length=17, blank=True) # Validators should be a list
    # indivisual = models.BooleanField(default=True, blank=True, null=True, choices=BOOLEB)
    # company = models.BooleanField(default=False, blank=True, null=True , choices=BOOLEB)
    # company_n = models.CharField(max_length=250, blank=True)
    # job_position = models.CharField(max_length=250, blank=True)
    
    def __str__(self):
        return self.f_name + " " + self.l_name









