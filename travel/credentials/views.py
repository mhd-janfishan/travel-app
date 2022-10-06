from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        luname=request.POST['name']
        lp=request.POST['password']
        user=auth.authenticate(username=luname,password=lp)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        uname=request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        p = request.POST['pass1']
        cp = request.POST['pass2']

        if p==cp:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'user name exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already used')
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,password=p,email=email,first_name=fname,last_name=lname)
                user.save()
                print("user created")
                return redirect('login')
        else:
           messages.info(request,"password not match")
           return redirect('register')
        return redirect('/')

    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')