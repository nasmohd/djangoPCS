from django import forms
from django.db import models

class StudentRegister(forms.Form):
	first_name = models.CharField(max_length=20)
	email = models.EmailField(max_length=50)
	password = models.CharField(max_length=50)