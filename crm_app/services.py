import imp
from employees.models import Employee
from settings.models import Currency
from leave.models import LeaveRecord
from .models import Customer
import datetime


def create_customer_instance(request):
    # Fetching data from the add new employee form
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    telephone = request.POST['telephone']
    

    
    # try:
    # Creating instance of Employee
    customer = Customer(first_name=first_name, last_name=last_name, email=email,
                        telephone=telephone,
                        )
    # Saving the employee instance
    customer.save()

  

    return customer

def edit_customer(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    telephone = request.POST['telephone']
    status = request.POST['status']

    customer = Customer(first_name=first_name, last_name=last_name, email=email,
                        telephone=telephone, status=status
                        )

    customer.save()

  

    return customer
