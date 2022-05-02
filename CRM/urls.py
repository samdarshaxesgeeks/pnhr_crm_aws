from cgitb import handler
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('ems_auth/', include('ems_auth.urls')),
    path('admin/', admin.site.urls),
    path('payroll/', include('payroll.urls')),
    path('leave/', include('leave.urls')),
    path('settings/', include('settings.urls')),
    path('overtime/', include('overtime.urls')),
    path('holidays/', include('holidays.urls')),
    path('', include('employees.urls')),
    path('ems_admin/', include('ems_admin.urls')),
    path('organisationdetails/', include('organisation_details.urls')),
    path('contract2/', include('contract2.urls')),
    path('notification/', include('notification.urls')),
    path('calendar/', include('cal.urls')),
    path('invoice/', include('invoice1.urls')),
    path('crm/', include('crm_app.urls')),
    path('contact/', include('contacts.urls')),
    # path('attendance/', include('attendance.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


handler404 = 'employees.views.error_404_view'