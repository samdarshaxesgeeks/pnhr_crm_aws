from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'contract'


urlpatterns = [
    path('', views.contractlist, name='contract'),
    path('add_contract', views.CreateContract, name='add_contract'),
    path('profile/<int:id>',views.profile,name="profile"),
    path('update_profile/<int:id>',views.update_profile,name="update_profile"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)