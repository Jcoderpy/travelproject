from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'The Password or Username is not correct')
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        a = request.POST['username']
        b = request.POST['first']
        c = request.POST['last']
        d = request.POST['email']
        e = request.POST['pass']
        f = request.POST['pass2']
        if e == f:
            if User.objects.filter(username=a).exists():
                messages.info(request,'User Name taken')
                return redirect('register')
            elif User.objects.filter(email=d).exists():

                messages.info(request,'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=a, first_name=b, last_name=c, email=d, password=e)

                user.save();
                return redirect ('login')
        else:
            messages.info(request,'password not match')
            return redirect('register')
        return redirect('/')

    return render(request, 'design.html')
def logout(request):
    auth.logout(request)
    return redirect('/')









