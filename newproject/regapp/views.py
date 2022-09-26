from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def registration(request):

    if request.method == 'POST':
        username = request.POST['username']
        F_name = request.POST['first_name']
        l_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_pwd = request.POST['password1']
        if password == confirm_pwd:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect("registration")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email taken")
                return redirect("registration")
            else:
                user = User.objects.create_user(username=username,first_name=F_name,last_name=l_name,email= email,password=password)
                user.save();
                # print("user created")
                return redirect('login')

        else:
            # print("password not matching")
             messages.info(request,"password not matching")
             return redirect('register')
        return redirect('/')
    return render(request, 'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not  None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid")
            return redirect('login')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
