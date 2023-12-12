from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import SendMessage
from .seralizers import EmailSerializer
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail

class EmailCreateView(generics.CreateAPIView):
    queryset = SendMessage.objects.all()
    serializer_class = EmailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    @receiver(post_save, sender=SendMessage)
    def send_message(sender, instance, created, **kwargs):
        if created:
                subject = "Новое письмо от "
                message = (
                           "Last Name: {}\n"
                           "First Name: {}\n"
                           "Middle Name: {}\n"
                           "IIN or BIN: {}\n"
                           "Email: {}\n"
                           "Phone Number: {}\n"
                           "Mail Address: {}\n"
                           "Questions: {} \n").format(
                        instance.last_name,
                        instance.first_name,
                        instance.middle_name,
                        instance.iin_or_bin,
                        instance.email,
                        instance.phone_number,
                        instance.mail_address,
                        instance.questions,
                )
                from_email = settings.EMAIL_HOST_USER
                recipient_list = ["s.esengeldinov@nzhkeden.kz"]

                send_mail(subject, message, from_email, recipient_list)
