from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.
def login(request):

    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid login')
            return redirect('foodapp1:login')

    return render(request, 'login.html')


def fun1(request):

        if request.method == 'POST':
            username = request.POST['username']
            firstname = request.POST['first_name']
            lastname = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            cpassword = request.POST['password1']

            if password==cpassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username already exits')
                    return redirect('foodapp1:register')

                if User.objects.filter(email=email).exists():
                    messages.info(request,'Email already exits')
                    return redirect('foodapp1:register')

                else:
                    user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,email=email, password=password)

                    user.save();
                    return redirect('foodapp1:login')


            else:
                messages.info(request,'password not matched')
                return redirect('foodapp1:register')
            return redirect('/')

        return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')