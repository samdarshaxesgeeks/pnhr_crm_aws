from django.db import models
from crm_app.models import Customer
from contacts.models import Contact
from django_countries.fields import CountryField
from invoice1.models import Invoice
from employees.models import Employee
from organisation_details.models import Team
from datetime import date
# from shop.models.product import BaseProductManager, BaseProduct


CONTRACT_STATUS = (
    ('Draft Contract', 'Draft Contract'),
    ('Working For Apparel', 'Working For Apparel'),
    ('Confermation', 'Confermation'),
    ('Done', 'Done'),
)
PAYMENT_MODE = (
    ('Chaque', 'Chaque'),
    ('Debit Card', 'Debit Card'),
    ('Cradit Card', 'Cradit Card'),
)

SERVICE_TYPE = (
    ('Business Visa', 'Business Visa'),
    ('Vsit Visa', 'Vsit Visa'),
    ('Investor Visa', 'Investor Visa'),
    ('Permanent Residency', 'Permanent Residency'),
    ('Work Permit', 'Work Permit'),

)





class Contract(models.Model):
   
    contract_no = models.CharField(max_length=200)
    create_date = models.DateField(("Date"),default=date.today)
    contract_date = models.DateField(null=True)
    customer = models.CharField(max_length=200)
    apply_company = models.CharField(max_length=200)
    service_type = models.CharField(max_length=200)
    service_Package  = models.CharField(max_length=200)
    contract_template = models.CharField(max_length=200, null=True, blank=True)
    Payment_Mode= models.CharField(max_length=50, null=True, blank=True)
    untaxed_amount=models.FloatField()
    tax_amount= models.FloatField()
    total=models.FloatField()

    def __str__(self):
        return self.contract_no



  



class Product(models.Model):
   
    contract_no = models.CharField(max_length=200)
    product = models.CharField(max_length=200,null=True, blank=True,)
    price = models.IntegerField(null=True, blank=True,default=None)
    qty = models.IntegerField(null=True, blank=True,default=None)
    Untaxed_Amount=models.IntegerField(null=True, blank=True)
    tax = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.contract_no



class document(models.Model):
    contract_no = models.CharField(max_length=200)
    CV_Resum= models.ImageField(null=True, blank=True,default=None)
    Passpost_Scan_Copy= models.ImageField(null=True, blank=True,default=None)
    Emirates_ID= models.ImageField(null=True, blank=True,default=None)
    Ntional_ID= models.ImageField(null=True, blank=True,default=None)
    Additional_Documen= models.ImageField(null=True, blank=True,default=None)

    

# class payment(models.Model):


class Other_info(models.Model):
    contract_no = models.CharField(max_length=200)
    salesmen = models.CharField( max_length=50, null=True, blank=True)
    sales_team = models.CharField( max_length=50, null=True , blank=True)
    company = models.CharField(max_length=50, blank=True)
    # online_signature= models.BooleanField(default=False ,null=True, blank=True)
    # online_payment = models.BooleanField(default=False, null=True, blank=True)
    customer_refrance= models.CharField( max_length=50 , blank=True)
    fiscal_position= models.CharField(max_length=50 ,null=True  , blank=True)
