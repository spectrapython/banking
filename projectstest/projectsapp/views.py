from django.http import HttpResponse

from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Branch,District


# Create your views here.
def home(request):
    city = Branch.objects.all()
    dis= District.objects.all()

    return render(request, 'home.html', {'city': city,'dis':dis})



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/form')
        else:
            messages.info(request,"invalid creditional")
            return redirect('/register')

    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:

            if User.objects.filter(username=username).exists():
                messages.info(request,"user name taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                return redirect('login')
            print("user create")
        else:
            messages.info(request,"password not match")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')
def form(request):
    if request.method == 'POST':
        pass
    distr = District.objects.all()
    branch1=Branch.objects.all()
    return render(request,'form.html',{'distr':distr,'branch1':branch1})




