from dataclasses import field
from django import forms

from .models import  Customer
# from contact import forms



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"



# class ContactForm(forms.ModelForm):
#     class Meta:
#       model= Add_more_detail
#       fields="__all__"





# from .models import Contact


# class ContactForm(forms.ModelForm):
#     class Meta:
#       model=Contact
#       fields="__all__"





        