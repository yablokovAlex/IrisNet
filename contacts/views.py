from django.shortcuts import redirect,render_to_response
from django.contrib.auth.models import User
from django.contrib import auth

def allUsers(request):
    return render_to_response('contacts.html', {'Users': User.objects.all(), 'username': auth.get_user(request).username, })
