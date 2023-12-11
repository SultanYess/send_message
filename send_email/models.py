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

@receiver(post_save, sender=SendMessage)
def send_message(sender, instance, created, **kwargs):
    if created:
            subject = "Новое письмо от "
            message = (
                       "Last Name: {}\n"
                       "First Name: {}\n"
                       "Middle Name: {}\n"
                       "IIN or BIN: {}\n"
                       "Email:{}\n"
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
            from_email = "sultanesengeldinovv@gmail.com"
            recipient_list = ["krivivativlad@gmail.com"]

            send_mail(subject, message, from_email, recipient_list)