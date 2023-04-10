from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Gymclass

# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        form=UserCreationForm()
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def Classes(request):
    gymclass=Gymclass.objects.all()
    return render(request,'gymclass.html',{'gymclass':gymclass})