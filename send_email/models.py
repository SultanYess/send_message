from django.conf import settings
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail



class SendMessage(models.Model):
    last_name = models.CharField(max_length=155, blank=False, default='')
    first_name = models.CharField(max_length=155, blank=False, default='')
    middle_name = models.CharField(max_length=155, blank=False, default='')
    iin_or_bin = models.CharField(max_length=155, blank=False, default='')
    email = models.EmailField()
    phone_number = models.CharField(max_length=155, blank=False, default='8')
    mail_address = models.EmailField(default='')
    questions = models.CharField(max_length=155, blank=False, default='')

    def __str__(self):
        return self.last_name
