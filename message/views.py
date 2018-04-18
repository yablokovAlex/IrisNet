from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth.models import User
from django.db.models import Count
from selenium import webdriver
from .models import Chat
import re
from django.template.context_processors import csrf
from .forms import MessageForm
from django.urls import reverse
from django.views import View


def send_message(request, chat_id):
    form = MessageForm(data=request.POST)
    if form.is_valid():
        message = form.save(commit=False)
        message.chat_id = chat_id
        message.author = request.user
        message.save()
    return redirect(reverse('users:messages', kwargs={'chat_id': chat_id}))


def create_dialog(request, user_id):
    chats = Chat.objects.filter(members__in=[request.user.id, user_id]).annotate(c=Count('members')).filter(c=2)
    if chats.count() == 0:
        chat = Chat.objects.create()
        chat.members.add(request.user)
        chat.members.add(user_id)
    else:
        chat = chats.first()
    return render_to_response('/dialog', {'chat_id': chat.id})


def parse_url():
    driver = webdriver.Chrome()
    return re.findall('\d+', driver)

def get_message(self, request, chat_id):
        try:
            chat = Chat.objects.get(id=chat_id)
            if request.user in chat.members.all():
                chat.message_set.filter(is_readed=False).exclude(author=request.user).update(is_readed=True)
            else:
                chat = None
        except Chat.DoesNotExist:
            chat = None

        return render(
            request,
            'messages/messages.html',
            {
                'user': request.user,
                'chat': chat,
                'form': MessageForm()
            }
        )
