from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Gymclass,User
from django.contrib.auth.views import LoginView

# Create your views here.
def home(request):
    return render(request,'home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            
            # log the user in
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid login credentials. Please try again."
            return render(request, 'signin.html', {'error_message': error_message})
    else:
        return render(request, 'signin.html')

def Classes(request):
    gymclass=Gymclass.objects.all()
    return render(request,'gymclass.html',{'gymclass':gymclass})

def singleclass(request,pk):
    gymclass=get_object_or_404(Gymclass,id=pk)
    
    print(gymclass)
    return render(request,'singleclass.html',{'gymclass': gymclass})