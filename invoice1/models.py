from django.db import models
from crm_app.models import Customer
from datetime import date
from crm_app.models import Customer



  

class Invoice(models.Model):

    invoice_no = models.CharField(max_length=200)
    invoice_date = models.DateField(null=True)
    
    #ship to
    s_name = models.CharField(max_length=200)
    s_email = models.EmailField(null=True)
    s_state = models.CharField(max_length=200)
    s_address = models.CharField(max_length=200)
    # Bill to
    b_name = models.CharField(max_length=200)
    b_email = models.EmailField(null=True)
    b_state = models.CharField(max_length=200)
    b_address = models.CharField(max_length=200)
    # placeofsupply'
    Address = models.CharField(max_length=200)
 
    def __str__(self):
        return str(self.invoice_no)

# extra add new
    sub_total = models.CharField(max_length=200,null=True, blank=True,default=None)
    tax_amount = models.CharField(max_length=200,null=True, blank=True,default=None)
    grand_total = models.CharField(max_length=200,null=True, blank=True,default=None)
    amount_deposit = models.CharField(max_length=200,null=True, blank=True,default=None)
    amount_due = models.CharField(max_length=200,null=True, blank=True,default=None)
class Product(models.Model):
    
    invoice_no = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.CharField(max_length=200,null=True, blank=True,)
    price = models.IntegerField(null=True, blank=True,default=None)
    qty = models.IntegerField(null=True, blank=True,default=None)
    tax = models.IntegerField(null=True, blank=True,default=None)
    total = models.IntegerField(null=True, blank=True,default=None)
    def __str__(self):
        return str(self.invoice_no)

