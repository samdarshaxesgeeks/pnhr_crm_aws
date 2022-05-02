from .models import Customer
from settings.selectors import get_ugx_currency, get_usd_currency




def get_customer(customer_id):
    return Customer.objects.get(pk=customer_id)


def get_customer_suspect():
    return Customer.objects.filter(status='Suspect')

def get_customer_prospect():
    return Customer.objects.filter(status='Prospect')

def get_customer_approch():
    return Customer.objects.filter(status='Approch')

def get_customer_negotiate():
    return Customer.objects.filter(status='Negotiate')

def get_customer_won():
    return Customer.objects.filter(status='Won')

def get_passive_customer():
    return Customer.objects.filter(status='Leave')



