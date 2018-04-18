from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.models import User
import urllib.request
from bs4 import BeautifulSoup
import re

def userprofile(request):
    return render_to_response('profile.html', {'user': User.objects.get(id = auth.get_user(request).id), 'username': auth.get_user(request).username,
                                                'id': auth.get_user(request).id, 'first_name': User.first_name, 'email': User.email})

def userprofile1(request):
    return render_to_response('userprofile.html', {'user': User.objects.get(id = int(parsehref())), 'username': User.objects.get(id = int(parsehref())).username,
                                                'id': User.objects.get(id = int(parsehref())).id, 'first_name': User.first_name, 'email': User.email})


def get_id_from_url(url):
    if url[-1] == '/':
        url = url[:-1]

    i = url.rindex('/') + 1
    return url[i:]

def parsehref():
    pattern = re.compile(r'href="(.*)">')
    html = urllib.request.urlopen('http://127.0.0.1:8000/contacts/')
    soup = BeautifulSoup(html, 'html.parser').find('div', class_='nav-item')
    return  re.findall('(\d+)',re.findall(pattern, str(soup))[1])