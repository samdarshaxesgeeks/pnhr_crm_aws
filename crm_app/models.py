from statistics import mode
from unicodedata import name
from xml.parsers.expat import model
from django.db import models
from django.core.validators import RegexValidator
from employees.models import Employee
# from contacts.models import Contact
from django.utils.translation import gettext_lazy   as _
from django_countries.fields import CountryField
from imagefield.fields import ImageField
from datetime import datetime
# from contacts.models import Contact
from contextlib import nullcontext
from secrets import choice
from xmlrpc.client import Boolean
from django.utils.timezone import timezone

from django.core.validators import RegexValidator

# Create your models here.



CUSTOMER_STATE = (
    ("Suspect","Suspect"),
    ("Prospect", "Prospect"),
    ("Approch", "Approch"),
    ("Negotiate", "Negotiate"),
    ("Won", "Won"),
)


class Customer(models.Model,):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30) 
    email = models.EmailField(max_length=250)
    telephone = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    telephone = models.CharField(validators=[telephone], max_length=17, blank=True) # Validators should be a list
    status = models.CharField(max_length=20, choices = CUSTOMER_STATE, default="Suspect")
    
    def __str__(self):
        return self.first_name + " " + self.last_name


class Allowance(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return "{}".format(self.name)



class Add_more_detail(models.Model):
    customer= models.ForeignKey(Customer , on_delete=models.CASCADE)
    # contact = models.OneToOneField(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CustomerDetails(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    c_date_of_birth = models.DateField()
    age = models.CharField(max_length=20)
    division = models.CharField(max_length=20)
    county = models.CharField(max_length=20)
    sub_county = models.CharField(max_length=20)
    passport_no = models.CharField(max_length=200, blank=True)
    village = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)


class CustomerBankDetail(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    name_of_bank = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    bank_account = models.CharField(max_length=20)

    def __str__(self):
        return "{} {}".format(self.name_of_bank, self.bank_account)

class CustomerSupervision(models.Model):
    salesman = models.ForeignKey(Employee, on_delete=models.CASCADE)
   




# for contacts function
# class Contact2(models.Model):
#     img = ImageField(upload_to='contact/', auto_add_fields=True, blank=True)
#     f_name = models.CharField(max_length=50)
#     l_name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=250)
#     gender = models.CharField(max_length=20)
#     per_address = models.CharField(max_length=250)
#     pr_country = CountryField()
#     cor_address = models.CharField(max_length=250)
#     cr_country = CountryField()
#     tax_id = models.CharField(max_length=150)
#     date_of_birth = models.DateField()
#     Age = models.IntegerField()
#     high_education = models.CharField(max_length=250)
#     occupation = models.CharField(max_length=150)
#     no_of_experience = models.IntegerField()
#     parent_f_name = models.CharField(max_length=50)
#     parent_l_name = models.CharField(max_length=50)
#     pas_no = models.CharField(max_length=16)
#     pas_country = CountryField()
#     telephone = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     telephone = models.CharField(validators=[telephone], max_length=17, blank=True) # Validators should be a list
#     # indivisual = models.BooleanField(default=True, blank=True, null=True, choices=BOOLEB)
#     # company = models.BooleanField(default=False, blank=True, null=True , choices=BOOLEB)
#     # company_n = models.CharField(max_length=250, blank=True)
#     # job_position = models.CharField(max_length=250, blank=True)
    
#     def __str__(self):
#         return self.f_name + " " + self.l_name

# for bank detelis 
class BankDetails(models.Model):
    customer_name = models.CharField(max_length=50)
    name_of_bank = models.CharField(max_length=20)
    branch= models.CharField(max_length=20)
    bank_account = models.CharField(max_length=20)

    def __str__(self):
        return (f"{self.name_of_bank} , {self.bank_account}")
        

