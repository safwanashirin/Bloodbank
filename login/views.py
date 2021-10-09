from typing import NamedTuple
from django.core.checks import messages
from django.http.response import HttpResponse, StreamingHttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth



# Create your views here.
l1=[]
ul=[]
def logout(request):
    auth.logout(request)
    return render(request, "LOG.html")
def first(request):
   return render(request, "firstpage.html")

def sign(request):
    if request.method == 'POST':
       
        username = request.POST['username'],
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,'username exits')
            return redirect(sign)
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save();
            print('user created')
            return redirect(login)
            
    else:
        return render(request, "SIGNUP.html")
        

def login(request):
    if request.method == 'POST':
        username = request.POST['username'],
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(add)
        else:
            messages.info(request, 'invalid credentials')
            return redirect(login)
    else:
        return render(request, "LOG.html")

def add(request):                         
    if request.method == 'POST':
        d1={
        "name" : request.POST['name'],
        "address" : request.POST['address'],
        "number" : request.POST['number'],
        "group" : request.POST['group']
        }
        l1.append(d1)
        return redirect('display')      
    else:
      return render(request, "home.html")

def display(request):
    return render(request, "display.html",{'data':l1})
    
    

