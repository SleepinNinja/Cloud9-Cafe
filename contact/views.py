from django.shortcuts import render
from home.views import Text
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from home.views import Image, Text
# Create your views here.

def contact(request):
    if request.method == 'POST':
        print(request.POST)
        if request.user.is_authenticated:
            sender = request.user.email

        else:
            sender = request.POST['sender-mail']

        reciever = [settings.EMAIL_HOST_USER,]
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(subject, message, sender, reciever)

        return HttpResponse('message_sent')

    else:
        contact_text = Text.objects.all().filter(page = "contact us")
        images = Image.objects.all().filter(page = 'contact us')

        section1_text = contact_text.get(section = 'section 1')
        print(len(section1_text.content.split('\n\n')))
        print(*section1_text.content.split('\n'), sep = '\n')
        print(*section1_text.content.split('\n\n'), sep = '\n')
        section21_text = contact_text.get(section = 'section 2.1')
        section22_text = contact_text.get(section = 'section 2.2')

        data = {
            'text': contact_text,
            'image': images.get(section = 'section 1'),
            'section2': images.get(section = 'section 2'),
            'section21': (section21_text.title, section21_text.content.split('\n')),
            'section22': (section22_text.title, section22_text.content.split('\n')),
        }

        return render(request, "contact.html", data)
