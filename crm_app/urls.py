from django.urls import path
from . import views

app_name = 'crm_app'

urlpatterns = [
    path('', views.crm_page, name='crm_page'),
    path('add_new_customer', views.add_new_customer, name='add_new_customer'),
    path('e_crm/<int:id>/', views.customer_page, name="customer_page"),
    path('customer_profile_page/<int:customer_id>/', views.customer_profile_page, name="customer_profile_page"),
    path('edit_customer_page/<int:id>/', views.edit_customer_page, name="edit_customer_page"),
    path('edit_customer/<int:id>', views.edit_customer, name="edit_customer"),
    path('msg', views.msg , name="msg"),
    path('delete_customer/<int:id>', views.delete_customer, name='delete_customer' ),
    
    path('add_new_contact/', views.add_new_contact, name='add_new_contact' ),
    path('edit_contact/', views.edit_contact, name='edit_contact' ),

    path('add_new_bank/', views.add_new_bank, name='add_new_bank' ),
    path('edit_bank/', views.edit_bank, name='edit_bank' ),
    path('add_salesmen/', views.add_salesmen, name='add_salesmen' ),
    ]


