from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Chat(models.Model):
    class Meta:
        db_table = 'chat'

    DIALOG = 'D'
    CHAT = 'C'
    CHAT_TYPE_CHOICES = (
        (DIALOG, 'Dialog'),
        (CHAT, 'Chat')
    )

    type = models.CharField(
        'Type',
        max_length=1,
        choices=CHAT_TYPE_CHOICES,
        default=DIALOG
    )

    members = models.ManyToManyField(User)




class Message(models.Model):
    class Meta:
        db_table = 'message'
        ordering = ['pub_date']

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text_message = models.TextField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now)
