from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileCreateForm,ProfileUpdateForm,AddressForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


def init(request):
	if request.method=='POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f'Your account has been created. Log in to use it!')
			return redirect('login')
	else:
		if request.user.is_authenticated:
			return redirect('users-home')
		else:	
			form = UserRegisterForm()
	return render(request,'users/init.html',{'form':form})


def login_view(request):
	if request.user.is_authenticated:
			return redirect('users-home')
	else:
		if request.method=='POST':
			form = AuthenticationForm(request,request.POST)
			if form.is_valid():
				username = form.cleaned_data.get('username')
				password = form.cleaned_data.get('password')
				user = authenticate(username=username,password=password)
				if user is not None:
					login(request,user)
					return redirect('users-home')
		else:
			form = AuthenticationForm()
		return render(request,'users/login.html',{'form':form})


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have been successfully logged out!")
    return render(request,'users/logout.html')


@login_required
def home(request):
	return render(request,'users/home.html')


@login_required
def profile(request):
	if request.user.profile.first_name=='':
		if request.method=='POST':
			form = ProfileCreateForm(request.POST,request.FILES,instance=request.user.profile)
			add_form = AddressForm(request.POST,instance=request.user.profile.address)
			if form.is_valid():
				form.save()
				add_form.save()
				messages.success(request,f'Your profile has been created!')
				return redirect('users-profile')
		else:
			form = ProfileCreateForm(instance=request.user.profile)
			add_form = AddressForm(instance=request.user.profile.address)
		return render(request,'users/new_profile.html',{'form':form,'add_form':add_form})
	else:
		return render(request,'users/profile.html')
	return render(request,'users/home.html')


@login_required
def update_profile(request):
	if request.method=='POST':
		u_form = UserUpdateForm(request.POST,instance=request.user)
		p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
		add_form = AddressForm(request.POST,instance=request.user.profile.address)
		if u_form.is_valid() and p_form.is_valid() and add_form.is_valid():
			u_form.save()
			p_form.save()
			add_form.save()
			messages.success(request,f'Your profile has been updated!')
			return redirect('users-profile')
				
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
		add_form = AddressForm(instance=request.user.profile.address)
	return render(request,'users/update_profile.html',{'u_form':u_form,
														'p_form':p_form,
														'add_form':add_form})