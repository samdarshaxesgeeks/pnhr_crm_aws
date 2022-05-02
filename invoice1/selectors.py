from .models import Invoice

def get_invoice(invoice_id):
    return Invoice.objects.get(pk=invoice_id)