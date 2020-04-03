from django.db import models

# Create your models here.
class Employee(models.Model):

	first_name = models.CharField(max_length=500)
	last_name = models.CharField(max_length=500)
	address = models.CharField(max_length=500)
	dob = models.CharField(max_length=12)
	title = models.CharField(max_length=500)
	Supervisor = models.CharField(max_length=500)
	phone = models.CharField(max_length=500)
	email = models.CharField(max_length=500)
	image_url = models.CharField(max_length=500)

	def __str__(self):
		return self.first_name + " " + self.last_name