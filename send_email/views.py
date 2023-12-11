from django.core.mail import send_mail
from rest_framework import generics, mixins
from .models import SendMessage
from .seralizers import EmailSerializer
from django.conf import settings
import logging


logger = logging.getLogger(__name__)
class EmailCreateView(generics.CreateAPIView):
    queryset = SendMessage.objects.all()
    serializer_class = EmailSerializer
