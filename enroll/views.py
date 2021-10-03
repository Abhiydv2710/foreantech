from django.shortcuts import render
from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from .models import User
# Create your views here.
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            cp=fm.cleaned_data['conformpassword']
            reg=User(name=nm,email=em,password=pw,conformpassword=cp)
            reg.save()
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    stud=User.objects.all()

    return render(request,'enroll/registration.html',{'form':fm,'stu':stud})

def user_login(request):
    if request.method=="POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname, password=upass)
            
        return render(request,'enroll/profile.html', {'form':fm})

    else:            

        fm=AuthenticationForm()
    return render(request,'enroll/login.html', {'form':fm})  

def user_profile(request):
    if request.method=='POST':
        fm=user_profile(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['propertyname']
            em=fm.cleaned_data['address']
            pw=fm.cleaned_data['details']
            print(nm)
            print(em)
            print(pw)
        else:
            fm=user_profile()
        return render(request,'enroll/profile.html',{'form':fm})      