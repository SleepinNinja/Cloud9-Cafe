from django.shortcuts import render
from home.models import Image, Text
from django.conf import settings
from django.conf.urls.static import static

# Create your views here.

def chefs(request):
    chefs_images = Image.objects.all().filter(page = 'chefs')
    chefs_text = Text.objects.all().filter(page = 'chefs')

    print(chefs_images, chefs_images.filter(section = 'meet our chefs'))

    data = {
        'chefs_images': chefs_images.filter(section = 'meet our chefs'),
        'text': chefs_text,
    }

    return render(request, "chefs.html", data)
