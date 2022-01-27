from genericpath import exists
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
# Create your views here.
def home(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard/admin')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect("/")

    else:
        return render(request,'login/login.html')  
def register(request):
    if request.method =='POST':
       username=request.POST['username']
       firstname=request.POST['firstname']
       lastname=request.POST['lastname']
       email=request.POST['email']
       password=request.POST['password']
       cpassword=request.POST['cpassword']
       if password==cpassword:
            if User.objects.filter(username=username).exists():

                messages.warning(request,'The username has already been taken')
                return redirect ('register')
            elif User.objects.filter(email=email).exists():
                messages.warning(request,'Email has already been taken')
                return redirect ('register')
            else:
                user= User.objects.create_user(username=username, first_name=firstname,last_name=lastname,email=email,password=password)
                user.save();
                return redirect("/")
       else: 
        messages.warning(request,'passwords do not match')
        return redirect ('register')
    else:

     return render(request,'login/register.html')

def dashboard(request):
    return render(request,'admin/pages/dashboard.html')
def logout_view(request):
    logout(request)
    return redirect("/")
    
