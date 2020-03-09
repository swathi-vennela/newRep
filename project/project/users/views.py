from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages      #for showing flash messages

def register(request):
	if request.method == 'POST':
			form = UserRegisterForm(request.POST)     #If we get a POST request, it instantiates a UserCreation form with the POST data
			if form.is_valid():                       #If the form data entered by the end user is valid, 
				form.save()
				username = form.cleaned_data.get('username')   #here we're grabbing the username into the variable 'username'. form.cleaned_data is a dictionary which contains the validated form data
				messages.success(request,f'Hey {username}! Your account has been created! You can login now!')  #show a flash message
				return redirect('login')   #after validating the form, we redirect the user to login page
	else:
			form = UserRegisterForm()    #If it is not a POST request, it just creates a blank form
	return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance= request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance= request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'Your account has been updated!')
			return redirect('profile')

	else:
		u_form = UserUpdateForm(instance= request.user)
		p_form = ProfileUpdateForm(instance= request.user.profile)

		context ={
		'u_form' : u_form,
		'p_form' : p_form
		}
	return render(request, 'users/profile.html', context)

