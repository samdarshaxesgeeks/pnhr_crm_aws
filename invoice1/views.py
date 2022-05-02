from django.shortcuts import render

# Create your views here.
from invoice1.models import Invoice,Product
from crm_app.models import Customer
from contacts.models import Contact
from .selectors import get_invoice
import datetime
from uuid import uuid4




def invoicelist(request): 

    # customer = Customer.object.all()
    # get_product = Product.objects.all().order_by('-pk')

    context={
        "invoice": Invoice.objects.all(),
        # 'product': get_product,
        # "invoice": "active",
        # "customer" : customer,
    }
    return render(request, 'invoice-table-list.html',context)



def CreateInvoice(request):
    # import pdb
    # pdb.set_trace()
    number = 'INVcd-' + str(uuid4()).split('-')[1]
    
    

    if request.method == 'POST':
        invoice_no = request.POST['invoice_no']
        b_name = request.POST['b_name']
        b_email = request.POST['b_email']
        b_state = request.POST['b_State']
        b_address = request.POST['b_Address']
     
        s_name = request.POST['s_name']
        s_email = request.POST['s_email']
        s_state = request.POST['s_State']
        s_address = request.POST['s_Address']
        
        Address = request.POST['Address']
        invoice_date = request.POST['date']

        #Product
        product = request.POST['product[]']
        price = request.POST['price[]']
        qty = request.POST['qty[]']
        tax = request.POST['tax1']
        total = request.POST['total[]']
        # total amount_0
        sub_total = request.POST['sub_total']
        tax_amount = request.POST['tax_amount']
        grand_total = request.POST['total_amount']
        amount_deposit = request.POST['amount_deposit']
        amount_due = request.POST['amount_due']
        invoice_obj = Invoice(invoice_no=invoice_no,b_name=b_name, b_email=b_email ,b_state=b_state,b_address=b_address,
                              s_name=s_name, s_email=s_email,s_state = s_state,s_address = s_address, invoice_date=invoice_date, Address=Address
                             ,grand_total=grand_total,amount_deposit=amount_deposit, sub_total=sub_total, amount_due=amount_due, tax_amount=tax_amount)
        invoice_obj.save()
        
        
        product_obj = Product( invoice_no=invoice_obj, product=product,price=price,qty=qty,tax=tax,total=total  )
       
        product_obj.save()
    context = {
        'number': number,
        "invoice": "active",

        # 'customer':customer
    }
    return render(request, 'create_invoice.html',context)


# edit invoice pages here

def invoic_edit_pages(request,id):
    inv=Invoice.objects.get(pk=id)
    context = {
        "crm_app":"active",
        "inv":inv
    }
    return render(request,"edit_invoice.html", context)



#for edit pages 
def edit_invoice(request, id):
    number = 'INVcd-' + str(uuid4()).split('-')[1]

    inv=Invoice.objects.get(pk=id)
    inv.invoice_no = request.POST['invoice_no']
    inv.b_name = request.POST['b_name']
    inv.b_email = request.POST['b_email']
    inv.b_state = request.POST['b_State']
    inv.b_address = request.POST['b_Address']
     
    inv.s_name = request.POST['s_name']
    inv.s_email = request.POST['s_email']
    inv.s_state = request.POST['s_State']
    inv.s_address = request.POST['s_Address']
        
    inv.Address = request.POST['Address']
    inv.invoice_date = request.POST['date']

        #Product
    inv.product = request.POST['product[]']
    inv.price = request.POST['price[]']
    inv.qty = request.POST['qty[]']
    inv.tax = request.POST['tax1']
    inv.total = request.POST['total[]']
        # total amount_0
    inv.sub_total = request.POST['sub_total']
    inv.tax_amount = request.POST['tax_amount']
    inv.grand_total = request.POST['total_amount']
    inv.amount_deposit = request.POST['amount_deposit']
    inv.amount_due = request.POST['amount_due']

    if request.method== 'POST':
        inv.save()
        context = {
            "inv":"active",
            "inv": inv,
            "number":number
        }
        return render(request, "success.html", context)
    # else:
    #     context = {
    #         "inv": "active",
    #         "failed_msg": "Failed! You performed a GET request"
    #     }

    #     return render(request, "c/contact_page.html", context)


  

#profile page for this 
def invoice_profile_page(request,   id):
    invoice= Invoice.objects.get(pk=id)
    product = Product.objects.filter(invoice_no=invoice)
    context = {
        "user": request.user,
        "invoice": "active",
        "invoice": invoice,
        "product": product,

    }
    return render(request, 'invoice_profile.html', context)

