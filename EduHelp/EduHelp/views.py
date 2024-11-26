from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from products.models import Course

def base(request):
    return render(request,'base.html')
def home(request):
    return render(request, 'components/home.html')