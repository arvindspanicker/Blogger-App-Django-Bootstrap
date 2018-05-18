from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
            first_name = request.POST['fname']
            last_name = request.POST['lname']
            email = request.POST['email']
            user_name = request.POST['username']
            pass_word = request.POST['password']
            confirm_p = request.POST['confirm']
            if confirm_p != pass_word:
                return render(request, 'blog/register.html')
            else:
                auth_user = User()
                auth_user.username = user_name
                auth_user.set_password(pass_word)
                auth_user.first_name = first_name
                auth_user.last_name = last_name
                auth_user.email = email
                auth_user.save()
                return HttpResponseRedirect('/login/')
    else:
        return render(request, 'blog/registration.html')

