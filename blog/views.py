from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
import json

# Create your views here.
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'blog/profile.html') 
    else:
        return HttpResponseRedirect('/login')

def home(request):
    if request.user.is_authenticated:
        return render(request, 'blog/home.html')
    else:
        return HttpResponseRedirect('/login')

def addblog(request):
    if request.user.is_authenticated:
        return render(request, 'blog/addblog.html')
    else:
        return HttpResponseRedirect('/login')

def blog(request):
    if request.user.is_authenticated:
        return render(request, 'blog/blog.html')
    else:
        return HttpResponseRedirect('/login')

def chat(request):
    if request.user.is_authenticated:
        return render(request, 'blog/chat.html')
    else:
        return HttpResponseRedirect('/login')