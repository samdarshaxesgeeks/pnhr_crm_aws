from django.contrib import admin
from .models import Contract, Product,Other_info,document

# Register your models here.


admin.site.register(Contract)
admin.site.register(Product)
admin.site.register(document)
admin.site.register(Other_info)



