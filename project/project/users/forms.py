from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):     #"UserCreationForm" in the paranthesis tells that this UserRegisterForm is being inherited from UserCreationForm
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()         #we need to specify this additional field because the email field is not there in the model User

	class Meta:
		model = User
		fields = ['username', 'email']
