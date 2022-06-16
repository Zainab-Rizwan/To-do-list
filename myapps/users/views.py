from django.shortcuts import render, redirect
from . forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def register(request):
	if request.method =='POST':
		#form with post data
		form= UserRegisterForm(request.POST)
		#data entered is valid
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created')
			return redirect('/login')
	else:
		form= UserRegisterForm()
	return render(request, 'users/registration.html', {'form':form})

@login_required
def profile(request):
 	return render(request, 'users/page.html')

