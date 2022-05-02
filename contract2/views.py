
from django.shortcuts import render,redirect
from crm_app.models import Customer
from .models import Contract, Product,Other_info,document
import random

# Create your views here


def contractlist(request):
    

    context={


    
        "cotract": "active",
        'contract':Contract.objects.all(),
        'customer': Customer.objects.all(),

    }

    return render(request, 'contract/contract-table-list.html',context)


def add_new_contract(request):
    if request.method == 'POST':
        customer = CreateContract(request)
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


def CreateContract(request):
    customer=Customer.objects.all()
   
    number = 'W-' + str(random.randint(10000000 , 99999999))
    print(number)
    # contract=get_object_or_404(Contract, pk=id)
    if request.method == 'POST':
        contract_no = number
        customer = request.POST['customer']
        contract_date =request.POST['contract_date'] 
        apply_company =request.POST['country']
        service_package =request.POST['service_Package']
        service_type = request.POST['services_type']
        contract_template = request.POST['contract_tamplate']
        Payment_Mode= request.POST.get('Payment_mode')
        untaxed_amount=request.POST.get('sub_total')
        tax_amount= request.POST.get('tax_amount')
        total_amount= request.POST.get('total_amount')
        

# product models here.
        # Product.contract=contracts
        product= request.POST['product[]']
        price= request.POST['price[]']
        qty= request.POST['qty[]']
        Untaxed_Amount= request.POST.get('total[]')
        tax= (request.POST.get('tax'))
        print(f" the tax is {tax}")
        total= request.POST['total[]']
        product_obj =Product(contract_no=contract_no,product=product,price=price,qty=qty,Untaxed_Amount=Untaxed_Amount,tax=tax,total=total) 

        # document model here
        CV_Resum= request.POST['resume']
        Passpost_Scan_Copy= request.POST['Passpost_Scan_Copy']
        print("shfsudfyerurdifhrh",Passpost_Scan_Copy)
        print("shfsudfyerurdifhrh",Passpost_Scan_Copy)
        Emirates_ID= request.POST['EmiratesID']
        Ntional_ID= request.POST.get('national_id')
        Additional_Documen= request.POST.get('Additional_Documents')
        print("dsuhgfusyfgsdf",Additional_Documen)
        print("dsuhgfusyfgsdf",Additional_Documen)

        Document=document(CV_Resum=CV_Resum,Passpost_Scan_Copy=Passpost_Scan_Copy,Emirates_ID=Emirates_ID,Ntional_ID=Ntional_ID,Additional_Documen=Additional_Documen)

        # other_info model here
        Salesperson= request.POST.get('Salesperson')
        sales_team=request.POST.get('sales_team')
        company= request.POST.get('company')
        # online_signature= request.POST.get('online_signature')
        # online_payment= request.POST.get('online_payment')
        customerrefrance= request.POST['customer_refrance']
        fiscal_position= request.POST.get('Fiscal_Position')

        other=Other_info(salesmen=Salesperson,sales_team=sales_team,company=company,customer_refrance=customerrefrance,fiscal_position=fiscal_position)

        c=Contract(contract_no=contract_no,contract_date=contract_date,customer=customer,apply_company=apply_company,service_Package=service_package,service_type=service_type,contract_template=contract_template,Payment_Mode=Payment_Mode,untaxed_amount=untaxed_amount,tax_amount=tax_amount,total=total_amount)
        
        c.save()


        print("saved Successfully")
        product_obj.save()
        print("product obj saved Successfully")
        Document.save()
        print("Document saved Successfully")
        other.save()
        print("other saved Successfully")
        

    context = {
        'number': number,
        "contract": "active",
        # 'contract':contract
        "customer":customer

    }
    return render(request, 'contract/create_contract.html',context)        
        


def profile(request, id):
    contract=Contract.objects.get(pk=id)
    product=Product.objects.filter(contract_no=contract)
    Document=document.objects.filter(contract_no=contract)
    other_info=Other_info.objects.filter(contract_no=contract)

    context = {
        "user" : request.user,
        "contract":"active",
        "contract": contract,
        "product": product,
        "Document": Document,
        "Other_info": other_info,
        

    }


    return render(request,'contract/profile.html', context)


def update_profile(request,id):
    # number = 'W-' + str(random.randint(10000000 , 99999999))
    contract=Contract.objects.get(pk=id)
    product=Product.objects.filter(contract_no=contract)
    Document=document.objects.filter(contract_no=contract)
    other_info=Other_info.objects.filter(contract_no=contract)

    # contract_no = number
    Contract.customer = request.POST.get('customer1')
    Contract.contract_date =request.POST.get('contract_date')
    Contract.apply_company =request.POST.get('country')
    Contract.service_package =request.POST.get('service_Package')
    Contract.service_type = request.POST.get('services_type')
    Contract.contract_template = request.POST.get('contract_tamplate')
    Contract.Payment_Mode= request.POST.get('Payment_mode')



# product models here.
    # Product.contract=contract_no
    product.product= request.POST.get('product[]')
    product.price= request.POST.get('price[]')
    qty= request.POST.get('qty[]')
    Untaxed_Amount= request.POST.get('total[]')
    tax= (request.POST.get('tax'))
    print(f" the tax is {tax}")
    total= request.POST.get('total[]')
    

    # document model here
    Document.Passpost_Scan_Copy= request.POST.get('Passpost_Scan_Copy')
    Document.Emirates_ID= request.POST.get('EmiratesID')
    Document.Ntional_ID= request.POST.get('national_id')
    Document.Additional_Documen= request.POST.get('Additional_Documents')

    # other_info model here
    other_info.Salesperson= request.POST.get('Salesperson')
    other_info.sales_team=request.POST.get('sales_team')
    other_info.company= request.POST.get('company')
    # online_signature= request.POST.ge('online_signature')
    # online_payment= request.POST.get('online_payment')
    other_info.customerrefrance= request.POST.get('customer_refrance')
    other_info.fiscal_position= request.POST.get('Fiscal_Position')

    # zippedList = zip(product,contract,Document,Other_info)

    return render(request, 'contract/update-profile.html')