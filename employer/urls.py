from django.urls import path
from . import views

urlpatterns = [
	path('',views.home_page, name='home_page'),
	path('add_employee', views.add_employee, name='add_employee'),
	path('edit_employee/<int:employee_id>', views.edit_employee, name='edit_employee'),
	path('delete_employee/<int:employee_id>', views.delete_employee, name='delete_employee'),
	]