from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Address

class UserRegisterForm(UserCreationForm):
	email=forms.EmailField()

	class Meta:
		model=User
		fields=['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
	email=forms.EmailField()

	class Meta:
		model=User
		fields=['username','email']


class ProfileCreateForm(forms.ModelForm):
	
	class Meta:
		model=Profile
		fields=['image','first_name','last_name','dob']


class AddressForm(forms.ModelForm):
	
	class Meta:
		model=Address
		fields=['city','state','country']

class ProfileUpdateForm(forms.ModelForm):
	
	class Meta:
		model=Profile
		fields=['image']