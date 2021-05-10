from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,"home.html")
def login(request):
    if request.method=="POST":
        user=auth.authenticate(username=request.POST['email'],password=request.POST['password'])
        if user is not None:
            return redirect('home')
        else:
            return render(request,'account/login.html',{'error':'Incorrect Username or Password'})
    else:
        return render(request ,'account/login.html')
def logout(request):
    if request.method=="POST":
        auth.logout(request)
        return redirect('home')
def signup(request):
    if request.method=="POST":
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user=User.objects.get(username=request.POST['email'])
                return render(request,'account/signup.html',{'error':'User already exist'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['email'],first_name=request.POST['fname'],last_name=request.POST['lname'],email=request.POST['email'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'account/signup.html',{'error':'password does not match'})
    else:
        return render(request,"account/signup.html")

