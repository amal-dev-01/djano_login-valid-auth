from django.shortcuts import render,redirect,HttpResponse
from .forms import StudentForm
# from django.contrib.auth.models import User
from .models import CustomUser
import re
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            phone_number=form.cleaned_data['phone_number']
            std = CustomUser.objects.create_user(username=username, email=email,password=password,phone_number=phone_number)
            print(username,password)
            std.save()
            return redirect('login')
        else:
           return render(request, 'signup.html', {'form': form})
    form=StudentForm()
    return render(request,'signup.html',{'form':form})


def login_page(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(username,password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse( 'Please check username and password.')
             
    return render(request,'login.html')   
@login_required(login_url='login')
def home(request):
    user=request.user
    return render(request,'home.html',{'username':user.username})

def logout_page(request):
    logout(request)
    return redirect("login")