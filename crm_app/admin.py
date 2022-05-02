from django.contrib import admin
from  .models import Customer, CustomerDetails, CustomerSupervision, CustomerBankDetail

# Register your models here.

admin.site.register(Customer)
admin.site.register(CustomerDetails)

admin.site.register(CustomerSupervision)
admin.site.register(CustomerBankDetail)
        
