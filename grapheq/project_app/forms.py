from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# creating custom user
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password1', 'first_name', 'last_name']