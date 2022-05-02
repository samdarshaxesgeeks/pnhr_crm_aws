import imp
from employees.models import Employee
from settings.models import Currency
from leave.models import LeaveRecord
from .models import Customer
import datetime
import random
from .models import Contract
from invoice1.models import Product


def create_contract_instance(request):
    # Fetching data from the add new employee form
    number = 'W-' + str(random.randint(10000000 , 99999999))
    # contract = Contract.objects.get()

    if request.method == 'POST':
        contract_no = request.POST['contract_no']
        create_date = request.POST['create_date']
        contract_date = request.POST['contract_date']
        customer = request.POST['customer']
        apply_country = request.POST['apply_country']
        sales_team = request.POST['sales_team']
        salesmen = request.POST['salesmen']
        contract_status = request.POST['contract_status']
        service_type = request.POST['service_type']
        contract_template = request.POST['contract_template']
     
        contract = Contract(contract_no = contract_no, create_date = create_date, contract_date = contract_date, customer = customer, apply_country = apply_country, sales_team = sales_team, salesmen = salesmen, contract_status = contract_status, service_type = service_type, contract_template = contract_template)

        contract.save()

        product = request.POST['product[]']
        price = request.POST['price[]']
        qty = request.POST['qty[]']
        tax = request.POST['tax1']
        total = request.POST['total[]']
        sub_total = request.POST['sub_total']
        tax_amount = request.POST['tax_amount']
        grand_total = request.POST['total_amount']
        amountdeposit = request.POST['amount_deposit']
        amountdue = request.POST['amount_due']

    
        product_obj = Product(amount_due=amountdue,amount_deposit=amountdeposit,
                              sub_total=sub_total,product=product,
                              price=price,qty=qty,tax=tax,total=total,tax_amount=tax_amount,
                              grand_total=grand_total)
 
    # 
    
        product_obj.save()
        
        return product_obj