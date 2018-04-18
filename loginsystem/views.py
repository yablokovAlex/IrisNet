from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from django.contrib import auth
from .forms import UserRegisterForm
from django.contrib.auth.models import User

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'The user is not found'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)

def register(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        if password2 == password1:
            user = User.objects.create_user(username, email=email, password = password1)
            user.save()
            auth.login(request,user)
            return redirect('/')
    return render_to_response('register.html', args)

