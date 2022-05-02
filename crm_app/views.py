from email import message
from multiprocessing import context
import re
from django.shortcuts import get_object_or_404, render,redirect
from crm_app.models import Customer, Allowance, CustomerDetails, CustomerBankDetail, CustomerSupervision
from employees.models import Employee
from employees.views import employee_page
from settings.selectors import get_all_currencies
from .selectors import get_customer, get_customer_suspect, get_passive_customer, get_customer_prospect, get_customer_approch, get_customer_won, get_customer_negotiate
from crm_app.services import create_customer_instance
from leave.forms.leave_record import LeaveRecordForm
from datetime import date
from organisation_details.models import Department, Position, Team, OrganisationDetail
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from contacts.models import Contact 
from .forms import CustomerForm

# Create your views here.


def crm_page(request):
    all_currencies = get_all_currencies()
    form = CustomerForm()
    context = {
        "user": request.user,
        "form":form,
        "currencies": all_currencies,
        "crm_app": "active",
        "customers_suspect": get_customer_suspect,
        "customers_prospect": get_customer_prospect,
        "customers_approch": get_customer_approch,
        "customers_negotiate": get_customer_negotiate,
        "customers_won": get_customer_won,
        "customers": Customer


    }
    return render(request, 'crm_app.html', context)


def add_new_customer(request):
    if request.method == 'POST':
        customer = create_customer_instance(request)
        context = {
            "crm_app": "active",
            "success_msg": "You have successfully added %s to the customer" % customer.first_name,
            "customer": customer
        }

        return render(request, 'success.html', context)

    else:
        context = {
            "crm_app": "active",
            "failed_msg": "Failed! You performed a GET request"
        }

        return render(request, "employees/failed.html", context)

def customer_page(request, id):
    
    employee = Employee.objects.get(pk=id)
    customer = Customer.objects.get(pk=id)
    yr = date.today().year


    context = {
        "user": request.user,
        
        "crm_app": "active",
        "customer": customer,
        "certifications": employee.certification_set.all(),
        "emergency_contacts": employee.emergencycontact_set.all(),
        "beneficiaries": employee.beneficiary_set.all(),
        "spouses": employee.spouse_set.all(),
        "dependants": employee.dependant_set.all(),
        "deps": Department.objects.all(),
        "titles": Position.objects.all(),
        "teams": Team.objects.all(),
        "allowances": Allowance.objects.all(),
   
    }
    return render(request, 'employees/employee.html', context)


from cal.forms import EventForm
from cal.models import Event

def customer_profile_page(request, customer_id):
    instance = Event()
    customer = get_customer(customer_id)
    status = customer.status


    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('cal:calendar'))
    context = {
        "user": request.user,
        "crm_app": "active",
        "customer": customer,
        "form" : form
    }

    return render(request, 'customer_profile.html', context)


def status_active(status):
    if status == ['suspect']:
        suspect = ["active"]
        return suspect
    
    elif status == ['prospect']:
        prospect = ["active"]
        return prospect
    
    elif status == ['approch']:
        approch = ["active"]
        return approch
    
    elif status == ['negotiate']:
        negotiate = ["active"]
        return negotiate
    elif status == ['won']:
        won = ["active"]
        return won





def edit_customer_page(request, id):
    customer = Customer.objects.get(pk=id)
    form = CustomerForm()
    context = {
        "form":form,
        "crm_app": "active",
        "customer": customer,
 
      
    }
    return render(request, 'edit_customer.html', context)


def edit_customer(request, id):

    obj = Customer.objects.get(pk=id)


    if request.method == 'POST':
        # Fetching data from the add new employee form
        customer = Customer.objects.get(pk=id)
        customer.title = request.POST['title']
        customer.first_name = request.POST['first_name']
        customer.last_name = request.POST['last_name']
        customer.email = request.POST['email']
        customer.telephone = request.POST['telephone']
        customer.status = request.POST['status']
        # customer.date_of_birth = request.POST['date_of_birth']
        # customer.c_age = request.POST['c_age']
        # customer.education = request.POST['education']
        # customer.occupation = request.POST['occupation']
        # customer.no_of_experience = request.POST['no_of_experience']
        # customer.permanent_address = request.POST['permanent_address']
        # customer.company = request.POST['company']
        # customer.apply_company = request.POST['apply_company']
        # customer.passport_no = request.POST['passport_no']
        # customer.service_type = request.POST['service_type']
      
        # customer.salesperson = request.POST['salesperson']
    

        # Saving the employee instance
        customer.save()
        context = {
            "crm_app": "active",
            "success_msg": "You have successfully updated %s's bio data" % (customer.first_name),
            "customer": customer,
            "obj":obj
        }

        return render(request, 'success.html', context)



    else:
        context = {
            "crm_app": "active",
            "failed_msg": "Failed! You performed a GET request"
        }

        return render(request, "failed.html", context)


def edit_more_details(request,id):
    customer = get_customer(id)
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name =request.POST.get('l_name')
        email = request.POST.get('Email') 
        gender =request.POST.get('Gender')
        per_address = request.POST.get('Permonent_Address')
        pr_country = request.POST.get('Parrment_Country')
        cor_address = request.POST.get('Current_Address')
        cr_country = request.POST.get('Current_Country')
        tax_id =request.POST.get('Tax_ID')
        date_of_birth = request.POST.get('dob')
        Age = request.POST.get('Age')
        high_education = request.POST.get('high_education')
        occupation = request.POST.get('Occupation')
        no_of_experience =request.POST.get('no_of_experience')
        parent_f_name = request.POST.get('parent_f_name')
        parent_l_name = request.POST.get('parent_l_name')
        pas_no = request.POST.get('passport_number')
        pas_country = request.POST.get('Passport_Country')
        telephone = request.POST.get('Telephone')
    
        obj= Contact(f_name=f_name, l_name=l_name,email=email,gender=gender,per_address=per_address,pr_country=pr_country,cor_address=cor_address,cr_country=cr_country,tax_id=tax_id, date_of_birth=date_of_birth,Age=Age,high_education=high_education,occupation=occupation,no_of_experience=no_of_experience,parent_f_name=parent_f_name,parent_l_name=parent_l_name,pas_no=pas_no, pas_country=pas_country,telephone=telephone)

        obj.save()
        


    context = {
        "user": request.user,
        "crm_page": "active",
        "customer": customer,
    }
    return render(request,"z.html", context)  

import requests
def send_message_on_whatsapp(mobile):

    url = "https://YOUR-WATI-ENDPOINT/api/v1/sendSessionMessage/"+mobile

    headers = {"Authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJhODMwMWYxOC0zZDJiLTQwZWQtOTBjZS1hNmVlY2NkOWFjNGYiLCJ1bmlxdWVfbmFtZSI6InBuaHJpbW1pdWFlQGdtYWlsLmNvbSIsIm5hbWVpZCI6InBuaHJpbW1pdWFlQGdtYWlsLmNvbSIsImVtYWlsIjoicG5ocmltbWl1YWVAZ21haWwuY29tIiwiYXV0aF90aW1lIjoiMDMvMzAvMjAyMiAwNzoxNDowNyIsImRiX25hbWUiOiI4NTA1IiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjoiQURNSU5JU1RSQVRPUiIsImV4cCI6MjUzNDAyMzAwODAwLCJpc3MiOiJDbGFyZV9BSSIsImF1ZCI6IkNsYXJlX0FJIn0.qIdZOYyTiEut5-LTMT-BIAQHGej_nt44sm_gRtofqvU","mobile":mobile}

    body = {'messageText': 'TEXTMESSSAGE'}

    response = requests.post(url,headers=headers, data = body)

    print(response.text)

def msg(request,telephone):
    customer = Customer.objects.all().order_by(telephone)
    telephone = customer.telephone

    context = {
        'telephone': telephone
    }
    send_message_on_whatsapp(telephone)
    return render(request,'customer_profile.html',context)




def delete_page(request,pk):
    pi=Customer.objects.get(id=pk)
    pi.delete()
    import pdb
    pdb.set_trace
    return redirect('/crm')
    # return render(request,'crm_app.html')


    







# def edit_more_details(request, customer_id):
#     customer = get_customer(customer_id)
#     # obj=Contact.objects.all()

#     context = {
#         "user": request.user,
#         "crm_app": "active",
#         "customer": customer,    

#     }
#     return render(request, 'z.html', context)




#bank delails Functions


def delete_customer(request, id):
    try:
        customer = Customer.objects.get(pk=id)
        name = customer.first_name + " " + customer.last_name
        customer_to_delete = customer
        customer_to_delete.delete()
    except Customer.DoesNotExist:
        context = {
            "crm_page": "active"
        }

        return render(request, 'deleted_customer.html', context)

    context = {
        "crm_page": "active",
        "deleted_msg": "You have deleted %s from customer" % (name),

    }
    return redirect('crm_app:crm_page')


def add_new_contact(request):
    if request.method == 'POST':
        customer_id = request.POST['customer_id']
        
        c_date_of_birth = request.POST['c_date_of_birth']
        age = request.POST['age']
        division = request.POST['division']
        county = request.POST['county']
        sub_county = request.POST['sub_county']
        # passport_no = request.POST['passport_no']
        village = request.POST['village']

        address = request.POST['address']
        telephone = request.POST['telephone']

        customer = Customer.objects.get(pk=customer_id)

        customerdetails = CustomerDetails(customer=customer,c_date_of_birth=c_date_of_birth,age=age,division=division,county=county,sub_county=sub_county,village=village,address=address,telephone=telephone, )

        customerdetails.save()

        context = {
            "crm_page" : "activate",
            "success_msg": "You have successfully added Home Address to the %s's details" % (customer.first_name),
            "customer": customer
        }

        return render(request, 'success.html', context)


def edit_contact(request):
    if request.method == 'POST':
        customer_id = request.POST['customer_id']
        customer = Customer.objects.get(pk=customer_id)

        customer_detail = CustomerDetails.objects.get(customer=customer)



        customer_detail.date_of_birth = request.POST['date_of_birth']
        customer_detail.age = request.POST['age']
        customer_detail.division = request.POST['division']
        customer_detail.county = request.POST['county']
        customer_detail.sub_county = request.POST['sub_county']
        customer_detail.parish = request.POST['parish']
        customer_detail.village = request.POST['village']

        customer_detail.address = request.POST['address']
        customer_detail.telephone = request.POST['telephone']

        customer = Customer.objects.get(pk=customer_id)

        customer_detail.save()

        context = {
            "crm_page" : "activate",
            "success_msg": "You have successfully added Home Address to the %s's details" % (customer.first_name),
            "customer": customer
        }

        return render(request, 'success.html', context)



def add_new_bank(request):
    if request.method == 'POST':
        # Fetching data from the add new home address form
        customer_id = request.POST['customer_id']
        name_of_bank = request.POST['bank_name']
        branch = request.POST['bank_branch']
        bank_account = request.POST['bank_account']

        # Get the employee instance
        customer = Customer.objects.get(pk=customer_id)
        # Creating instance of Bank Detail
        bank_detail = CustomerBankDetail(customer=customer, name_of_bank=name_of_bank, branch=branch, bank_account=bank_account)
        # Saving the BankDetail instance
        bank_detail.save()
        context = {
            "crm_page": "active",
            "success_msg": "You have successfully added %s Bank Details " % customer.first_name,
            "customer": customer
        }

        return render(request, 'success.html', context)

    else:
        context = {
            "customer_page": "active",
            "failed_msg": "Failed! You performed a GET request"
        }

        return render(request, "failed.html", context)


def edit_bank(request):
    if request.method == 'POST':
        # Fetching data from the edit home address form

        # Fetch the customer
        customer_id = request.POST['customer_id']
        customer = Customer.objects.get(pk=customer_id)
        # Grab the Bankdetail
        bank_detail = CustomerBankDetail.objects.get(customer=customer)

        bank_detail.name_of_bank = request.POST['bank_name']
        bank_detail.branch = request.POST['bank_branch']
        bank_detail.bank_account = request.POST['bank_account']

        # Saving the bank detail instance
        bank_detail.save()
        context = {
            "crm    _page": "active",
            "success_msg": "You have successfully updated %s's Bank Details" % (customer.first_name),
            "customer": customer
        }

        return render(request, 'success.html', context)

    else:
        context = {
            "crm_page": "active",
            "failed_msg": "Failed! You performed a GET request"
        }

        return render(request, "failed.html", context)


def add_salesmen(request):
    if request.method == 'POST':
        # Fetching data from the add deductions' form
        salesmanee_id = request.POST['supervisee_id']
        customer_id = request.POST['customer_id']

        # Fetch employee instance
        customer = Customer.objects.get(pk=customer_id)

        # Fetch employee instance of type supervisee
        salesman = Customer.objects.get(pk=salesmanee_id)

        # Create instance of supervision
        supervision = CustomerSupervision(salesman=salesman)
        # Save supervision instance
        supervision.save()
        context = {
            "employees_page": "active",
            "success_msg": "You have successfully added %s to the supervisees" % (supervision.supervisee),
            "customer": customer
        }

        return render(request, 'success.html', context)

    else:
        context = {
            "employees_page": "active",
            "failed_msg": "Failed! You performed a GET request"
        }

        return render(request, "failed.html", context)