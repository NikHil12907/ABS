from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def home(request):
    return render(request, 'theme/home.html')

def user_register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request,user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form':form})
            
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have Successfully logged in')
                return redirect('home')
            else:
                messages.error(request, 'Invalid Crendentials')
        else:
            messages.error(request, 'Invalid Form Submission')
    else:
        form = AuthenticationForm(request)
    return render(request, 'users/login.html', {'form':form})
        
