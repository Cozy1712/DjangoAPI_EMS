from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # Department url
    path(r'department', views.departmentApi),
    path(r'department/<int:id>', views.departmentApi),
    
    # Employees url
    path(r'employee', views.employeeApi),
    path(r'employee/<int:id>', views.employeeApi),
    
    path(r'employee/saveFile', views.saveFile),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
