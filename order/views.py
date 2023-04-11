from django.shortcuts import render, redirect

# Create your views here.
from .models import Cart, CartItem, Order
from menu.models import MenuItem
from datetime import datetime
from django.http import HttpResponse
from home.views import Image, Text


def remove_item(request):
    user_cart =  Cart.objects.all().filter(user = request.user)
    last_index = user_cart.count() - 1

    if last_index < 0:
        last_index += 1

    last_cart_items = user_cart[last_index].cartitem_set.all()

    selected_item_id = request.GET.get('item_id')
    removed_item = last_cart_items.get(pk = selected_item_id)
    removed_item.delete()

    return HttpResponse("Item removed")


def order(request):
    user_cart =  Cart.objects.all().filter(user = request.user)
    last_index = user_cart.count() - 1

    if last_index < 0:
        last_index += 1

    last_cart_items = user_cart[last_index].cartitem_set.all()
    total_price = sum([item.total_price for item in last_cart_items])
    gst = int(total_price * 0.18)

    user_orders = Order.objects.all().filter(user = request.user)

    pending_orders = user_orders.filter(status = 'ordered')

    completed_orders = user_orders.filter(status = 'completed')
    completed_orders_length = completed_orders.count()

    canceled_orders = user_orders.filter(status = 'canceled')
    canceled_orders_length = canceled_orders.count()

    if completed_orders_length < 3:
        last_3_completed = completed_orders

    else:
        last_3_completed = completed_orders[completed_orders_length - 3: completed_orders_length]

    if canceled_orders_length < 3:
        last_3_canceled = canceled_orders

    else:
        last_3_canceled = canceled_orders[canceled_orders_length - 3: canceled_orders_length]

    print(pending_orders, last_3_completed, last_3_canceled)

    section1_text = Text.objects.all().filter(page = 'order').get(section = 'section 1')

    image = Image.objects.get(page = 'orders')

    data = {
        'pending_orders': pending_orders,
        'completed_orders': last_3_completed,
        'canceled_orders': last_3_canceled,
        'cart_items': last_cart_items,
        'user': request.user,
        'total_price': total_price,
        'gst': gst,
        'image': image,
        'section1': (section1_text.title, section1_text.content.split('\n')),
    }

    return render(request, 'order.html', data)


def clear(request):
    user_carts = Cart.objects.all().filter(user = request.user)
    last_index = user_carts.count() - 1

    if last_index < 0:
        last_index += 1

    last_cart = user_carts[last_index]
    last_cart.cartitem_set.all().delete()

    return redirect(order)


def ordered(request):
    print(request.GET)

    image = Image.objects.get(page = 'welcome')
    user_carts = Cart.objects.all().filter(user = request.user)
    last_index = user_carts.count() - 1
    last_cart = user_carts[last_index]
    last_cart.checked_out = True
    last_cart.save()

    delivery_time = request.GET['delivery_time']
    total_price = request.GET['total_price']
    print(delivery_time, total_price)

    order_date = datetime.now()

    Order.objects.create(order_date = order_date, user = request.user, cart = last_cart,
    status = 'ordered', total_price = total_price, delivery_time = delivery_time)

    new_cart = Cart(user = request.user)
    new_cart.save()

    section1_text = Text.objects.all().filter(page = 'welcome').get(section = 'section 1')

    return render(request, 'welcome.html', {
    'image': image,
    'section1': (section1_text.title, section1_text.content.split('\n'))
    })
