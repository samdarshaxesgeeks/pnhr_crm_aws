from nturl2path import url2pathname
from django.urls import path
from . import views

app_name = 'invoice'


urlpatterns = [
    path('', views.invoicelist, name='invoice'),
    path('edit_invoice/<int:id>', views.edit_invoice, name="edit_invoice"),
    # path('edit_invoice', views.edit_invoice, name='edit_invoice'),
    path('add_invoice', views.CreateInvoice, name='add_invoice'),
    path('invoice_profile_page/<int:id>/', views.invoice_profile_page, name="invoice_profile_page"),
]

