from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegiForm
# Create your views here.
def register(response):

	if response.method == 'POST':
		form = RegiForm(response.POST)
		if form.is_valid():
			form.save()
			return redirect('Home')
	else:
		form = RegiForm()
	My_dict = {"form":form}
	return render(response, 'register/register.html', My_dict )