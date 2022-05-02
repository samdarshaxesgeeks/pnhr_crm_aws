from ast import Return
from django.shortcuts import redirect, render
from ems_auth.models import User
from .models import Contact
from django import forms
from django.http import HttpResponseRedirect
from .services import create_contact
from django.urls import reverse
from django_countries.fields import CountryField
from django.http import HttpResponseRedirect,HttpResponse
from .forms import ContactForm
# Create your views here.
# contact = Contact.objects.all()

# def contact_page(request):
#     form=ContactForm(request.POST)

#     country = CountryField()
#     context = {

#         "contact":contact,
#         "contact_page":"active",
#         "form":form,
#     }

#     return render(request, 'contact/contact_page.html', context)




def contact_page(request):
    country = CountryField()
    contact_get = Contact.objects.all()
    form=ContactForm(request.POST)
    context = {

        "contact":contact_get,
        "contact_page":"active",
        "country":country,
        "form":form,

    }

    return render(request, 'contact/contact_page.html', context)





# this factions will work add new data and show data from the add

def add_new_contact(request):    
    if request.method == 'POST':
        contact = create_contact(request)
        context = {
            "contact_page": "active",
            "success_msg": "You have successfully added %s to the contact" % contact.f_name,
            "contact": contact
        }
        return render(request, 'contact/success.html', context)

    else:
        context = {
            "contact_page": "active",
            "failed_msg": "Failed! You performed a GET request"
        }

        return render(request, "contact/contact_page.html", context)







def edit_contact_page(request, id):
    contact = Contact.objects.get(pk=id)
    context = {
        "contact": "active",
        "contact": contact
 
      
    }
    return render(request, 'contact/edit_contact.html', context)


def edit_contact(request, id):
    contact = Contact.objects.get(pk=id)
    contact.title = request.POST['title']
    contact.f_name = request.POST['f_name']
    contact.l_name = request.POST['l_name']
    contact.email = request.POST['email']
    contact.telephone = request.POST['telephone']
    contact.gender = request.POST['gender']
    contact.date_of_birth = request.POST['date_of_birth']
    contact.per_address = request.POST['per_address']
    contact.pr_country = request.POST['pr_country']
    contact.cor_address = request.POST['cor_address']
    contact.cr_country = request.POST['cr_country']
    contact.Age = request.POST['Age']
    contact.tax_id = request.POST['tax_id']
    contact.high_education = request.POST['high_education']
    contact.occupation = request.POST['occupation']
    contact.no_of_experience = request.POST['no_of_experience']
    contact.parent_f_name = request.POST['parent_f_name']
    contact.parent_l_name = request.POST['parent_l_name']
    contact.pas_no = request.POST['pas_no']
    contact.pas_country = request.POST['pas_country']
    contact.telephone = request.POST['telephone']


    if request.method == 'POST':
        # Fetching data from the add new employee form
        contact.save()
        context = {
            "contact": "active",
            "success_msg": "You have successfully updated %s's bio data" % (contact.f_name),
            "contact": contact,
        }

        return render(request, 'contact/success.html', context)
    else:
        context = {
            "contact": "active",
            "failed_msg": "Failed! You performed a GET request"
        }

        return render(request, "contact/contact_page.html", context)

def contact_profile_page(request, contact_id):
    
    contact = Contact.objects.get(pk=contact_id)



    
    context = {
        "user": request.user,
        "contact": "active",
        "contact": contact,
    }

    return render(request, 'contact/contact_profile.html', context)



def delete_page(request,id):
    pi=Contact.objects.get(id=id)
    pi.delete()
   
    return redirect('/contact')


