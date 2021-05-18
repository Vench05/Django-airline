from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout, forms
from .forms import SignUpForm
from flights import views

# Create your views here.
def index(request: HttpRequest):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    return render(request, 'users/index.html')

def login_view(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'users/login.html', {
                'message': 'Invalid credentials.'
            })

    return render(request, 'users/login.html')

def logout_view(request: HttpRequest):
    logout(request)
    return render(request, 'users/login.html', {
        'message': 'Logged Out'
    })

def signup_view(request: HttpRequest):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        print(form.error_messages)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) 
            login(request, user)
            return HttpResponseRedirect(reverse('flights'))
    return render(request, 'users/signup.html', {
        'form': form
    })