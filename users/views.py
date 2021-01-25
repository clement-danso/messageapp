from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegisterFrom
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from smsapp.decorators import *
# Create your views here.
@unauthenticated_user
def register(request):
	if request.method == 'POST':
		form = UserRegisterFrom(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, "%s, you're are now registered! Please login to continue." % username)
			
			return redirect('/login')
			
	else:
		form = UserRegisterFrom()
	
	return render(request, 'users/register.html', {'form': form})

@unauthenticated_user
def loginpage(request):
	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		
		user=authenticate(request, username=username, password=password)
		print(user)
		if user is not None:
			login(request, user)
			return redirect('/home')
		
		else:
			messages.success(request, "Sorry, either your username or password is incorrect!")
			fom = AuthenticationForm()
	else:
		fom = AuthenticationForm()		
			
			
			
	return render(request, 'users/login.html', {'fom': fom})

@login_required
def logoutuser(request):
	logout(request)
	messages.success(request, "Successfully logged out!")
	return redirect('/login')
