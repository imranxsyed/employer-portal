from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from employer.models import Employee
from django.db import models
# Create your views here.

def home_page(request):
	data = Employee.objects.all()
	print(data)
	return render(request,"employer/home_page.html", {"employees": data})

def add_employee(request):

	if request.method == 'GET':
		return  redirect(reverse('home_page'))

	elif request.method == 'POST':
		first_name = request.POST['first-name']
		last_name = request.POST['last-name']
		dob = request.POST['dob']
		url = request.POST['picture']
		email = request.POST['email']
		phone = request.POST['phone-number']
		address = request.POST['address']
		title = request.POST['title']
		supervisor = request.POST['reports-to']

		new_employee = Employee(
		  first_name	= first_name,
		  last_name		= last_name,
		  address		= address,
		  dob			= dob,
		  title 		= title,
		  Supervisor    = supervisor,
		  phone 		= phone,
		  email         = email,
		  image_url	= url
  		)

		
		new_employee.save()
		print("New Employee Saved successfully")
		return redirect(reverse('home_page'))


def edit_employee(request,employee_id):
	
	if request.method == "GET":
		render(reverse('home_page'))
	else:
		#retrieve an object
		employee = Employee.objects.get(pk=employee_id)
		#update fields
		employee.first_name = request.POST['first-name']
		employee.last_name = request.POST['last-name']
		employee.dob = request.POST['dob']
		employee.image_url = request.POST['picture']
		employee.email = request.POST['email']
		employee.phone = request.POST['phone-number']
		employee.address = request.POST['address']
		employee.title = request.POST['title']
		employee.Supervisor = request.POST['reports-to']
		#save the object
		employee.save();
		print("Employee Edited successfully!!")
	return redirect(reverse('home_page'))

def delete_employee(request,employee_id):
	employee = Employee.objects.get(pk=employee_id)
	employee.delete()
	return redirect(reverse('home_page'))
