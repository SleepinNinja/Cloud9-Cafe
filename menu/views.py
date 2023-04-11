from django.shortcuts import render, redirect
from . import models
from .models import MenuType, MenuItem
from home.models import Image, Text
from order.models import Cart, CartItem
from django.contrib.auth.models import User
from home.views import register
from django.contrib import messages
from django.http import HttpResponse
from home.views import register

# Create your views here.

def menu(request):
    types = MenuType.objects.all()
    images = Image.objects.all().filter(page = 'menu')

    menu_text = Text.objects.all().filter(page = 'menu')
    section1_text = menu_text.get(section = 'section 1')
    section2_text = menu_text.get(section = 'section 2')

    #print(*[image.image for image in images], sep = "\n")

    data = {
        'types': types,
        'section1': images.get(section = 'section 1'),
        'section2': images.get(section = 'section 2'),
        'section1_text': (section1_text.title, section1_text.content.split('\n')),
        'section2_text': (section2_text.title, section2_text.content.split('\n')),

    }

    return render(request, "menu.html", data)


def menu_display(request, type):
    print('inside of menu display', type)
    menu_type = MenuType.objects.filter(name = type)[0]
    menu_items = menu_type.menuitem_set.all()
    item_count = menu_items.count()

    image = Image.objects.filter(page = type)
    section1 = Text.objects.filter(page = type).get(section = 'section 1')

    data = {
        'menu_items': menu_items,
        'menu_type': menu_type,
        'section1': image.get(section = 'section 1'),
        'section2': image.get(section = 'section 2'),
        'section1_text': (section1.title, section1.content.split('\n'))
        }


    return render(request, 'menu_display.html', data)

def add_item(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            carts = Cart.objects.all()
            user_cart = carts.filter(user = request.user)
            last_index = user_cart.count() - 1

            if last_index < 0:
                last_index += 1

            last_user_cart = user_cart[last_index]

            if last_user_cart.checked_out:
                new_cart = Cart(user = request.user)
                new_cart.save()

                cart = new_cart

            else:
                cart = last_user_cart

            print(cart)

            item_id = request.POST['item_id']
            item = MenuItem.objects.get(pk = item_id)

            item_quantity = int(request.POST['quantity'])
            #item_quantity = 1
            total_price = item.price * item_quantity

            CartItem.objects.create(quantity = item_quantity, total_price = total_price, item = item, cart = cart)
            #print(request.user.username, cart.cartitem_set.all(), sep = '\n')
            #print("redirecting to the user to the menu page")
            return HttpResponse('Item added to cart')

        else:
            return HttpResponse('False')
