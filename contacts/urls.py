from django.urls import path
from  . import views
from django.conf import settings  
from django.conf.urls.static import static  


app_name = 'contact'


urlpatterns = [
    path('', views.contact_page, name ="contact_page"),
    
    path('edit_contact_page/<int:id>/', views.edit_contact_page, name="edit_contact_page"),
    path('edit_contact/<int:id>', views.edit_contact, name="edit_contact"),
    path('contact_profile_page/<int:contact_id>/', views.contact_profile_page, name="contact_profile_page"),
    #process
    path('add_new_contact/', views.add_new_contact, name='add_new_contact'),
    path('delete_contact/<int:id>/', views.delete_page, name="delete_contact"),
]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 