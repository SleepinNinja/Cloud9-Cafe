from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Text, Image, ProfilePhoto, Review
from order.models import Cart, Order
from django.http import HttpResponse
from order.views import order
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
import re, random


# Create your views here.
def cart_counter(request):
    user_cart =  Cart.objects.all().filter(user = request.user)
    last_index = user_cart.count() - 1

    if last_index < 0:
        last_index += 1

    last_cart_items = user_cart[last_index].cartitem_set.all()

    return HttpResponse(last_cart_items.count())


def home(request):
    home_images = Image.objects.all().filter(page = 'home')

    reviews = Review.objects.all()
    reviews_length = reviews.count()

    if reviews_length < 7:
        last_7 = reviews

    else:
        last_7 = reviews[reviews_length - 7, reviews_length]

    print(home_images)

    reviews = [(review, ProfilePhoto.objects.get(user = review.user).profile_photo)
        for review in last_7]

    print(reviews)

    section1 = Text.objects.filter(page = 'home').get(section = 'section 1')

    print(section1.content.split('\n'))

    data = {
        #'special_section': special_section,
        #'our_story': our_story[0].content.split('\n'),
        'section1_image': home_images[0],
        'reviews': reviews,
        'text': (section1.title, section1.content.split('\n')),
    }

    return render(request, "home.html", data)


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        print(username, password)

        user = auth.authenticate(username = username, password = password)
        print(user)

        if user is not None:
            auth.login(request, user)
            #messages.info(request, "User Logged In Successfully!!")
            return HttpResponse(True)

        else:
            return HttpResponse(False)

    image = Image.objects.get(page = 'login')

    return render(request, 'login.html', {'image': image})


def forgot_password(request):
    print(request.POST)

    if request.method == 'POST':
        action = request.POST['action']

        if action == 'validate-user':
            username = request.POST['username']
            user_check = User.objects.all().filter(username = username)

            response = 'valid' if user_check.count() != 0 else 'invalid'

            if response == 'valid':
                email = User.objects.get(username = username).email
                return HttpResponse(email)

            return HttpResponse(response)


        elif action == 'send-otp':
            email = request.POST['email']
            otp = random.randint(1000, 9999)
            sender = settings.EMAIL_HOST_USER
            recievers = [email,]
            subject = 'Password Reset OTP'
            message = 'Your password reset OTP is: ' + str(otp)

            send_mail(subject, message, sender, recievers)

            return HttpResponse(otp)

        elif action == 'reset-password':
            username = request.POST['username']
            user = User.objects.get(username = username)
            new_password = request.POST['password']
            user.set_password(new_password)
            user.save()

            return HttpResponse('Password change successful')

    else:
        image = Image.objects.filter(page = 'forgot password')
        image11 = image.get(section = 'section 1.1')
        image12 = image.get(section = 'section 1.2')

        return render(request, 'forgot_password.html', {
            'image11': image11,
            'image12': image12,
            })


def logout(request):
    auth.logout(request)
    messages.info(request, "User Logged Out Successfully!!")
    return redirect(home)


def user_profile(request, username):
    user = request.user
    images = Image.objects.all().filter(page = 'user')
    image1 = images.get(section = 'section 1')
    image_section2 = images.get(section = 'section 2')
    user_text = Text.objects.all().filter(page = 'user')
    section21_text = user_text.get(section = 'section 2.1')
    section22_text = user_text.get(section = 'section 2.2')
    section2_image = images.get(section = 'section 2')

    data = {
        'name': user.first_name,
        'username': user.username,
        'email': user.email,
        'profile_photo': ProfilePhoto.objects.get(user = user).profile_photo,
        'image': image1,
        'image_section2': image_section2,
        'section21': (section21_text.title, section21_text.content.split('\n')),
        'section22': (section22_text.title, section22_text.content.split('\n')),
    }

    return render(request, 'user_profile.html', data)


def register(request):
    if request.method == "POST":
        email = request.POST['email']
        otp = random.randint(1000,10000);

        sender_mail = settings.EMAIL_HOST_USER
        reciever_mails = [email,]
        subject = 'OTP Verification'
        message = f'Your OTP is: {otp}'
        print('otp', otp)

        try:
            send_mail(subject, message, sender_mail, reciever_mails)
            return HttpResponse(otp)

        except:
            return HttpResponse(False)

    else:
        images = Image.objects.all().filter(page = 'register')
        display_image = images.get(section = 'section 1.1')
        register_image = images.get(section = 'section 1.2')
        register_text = Text.objects.all().filter(page = 'register').get(section = 'section 1')

        return render(request, 'register.html', {
            'image': display_image,
            'register_image': register_image,
            'register_text': (register_text.title, register_text.content.split('\n')),
        })


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        new_user = User.objects.create_user(username = username , first_name = name, email = email, password = password)
        Cart.objects.create(user = new_user)
        ProfilePhoto.objects.create(user = new_user)

        return HttpResponse(f'User {username} created successfully')


def username_available(request):
    print('inside username available')

    if request.method == 'POST':
        username = request.POST['username']

        if request.user.username != username:
            occupied = User.objects.filter(username = username)
            is_available = True if occupied.count() == 0 else False

            return HttpResponse(is_available)

        else:
            return HttpResponse(True)


def change_info(request, username):
    user = request.user

    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']

        print(request.FILES)
        #print(request.POST['profile_photo'], request.FILES['profile_photo'])

        if len(request.FILES) > 0:
            upload = request.FILES['profile_photo']
            fss = FileSystemStorage(location = settings.MEDIA_ROOT + 'profile_img/', base_url =  '/profile_img/')
            file = fss.save(request.user.username + "_" + upload.name, upload)
            file_url = fss.url(file)
            print(file, file_url)
            print(username, name, email, upload)

            user_profile = ProfilePhoto.objects.get(user = request.user)
            user_profile.profile_photo = file_url

            user_profile.save()


        user.username = username
        user.first_name = name
        user.email = email

        print(username, name, email, user, user.username, user.first_name, user.email)

        user.save()

        return HttpResponse(True)


        #email_verification = re.compile(r'[a-zA-z0-9]+@[a-zA-Z0-9]*\.mes\.ac\.in')

        """
        if re.match(email_verification, user.email) != None:
            user.username = username
            user.first_name = name
            user.email = email
            user.save()

            messages.info(request, 'Changes have been Saved!')
            return redirect(user_profile, username = username)

        else:
            messages.info(request, 'Please Enter valid MES Id')
        """

    info = {
        'user': user,
        'profile_image': ProfilePhoto.objects.get(user = request.user).profile_photo,
    }

    return render(request, 'change_info.html', info)


def manage_order(request, order_type):
    orders = Order.objects.all()
    order_data = orders.filter(status = order_type)

    #pending_orders = orders.filter(status = 'ordered')
    #completed_orders = orders.filter(status = 'completed')
    #canceled_orders = orders.filter(status = 'canceled')

    #print(pending_orders, completed_orders, canceled_orders)

    if order_type == 'ordered':
        border = 'border-warning'
        order_data.order_by('delivery_time')

    elif order_type == 'canceled':
        border = 'border-danger'
        order_data.order_by('id')

    elif order_type == 'completed':
        border = 'border-success'
        order_data.order_by('id')

    data = {
        'order_data': order_data,
        'order_type': order_type,
        'border': border,
    }

    return render(request, 'manage_order.html', data)


def action(request):
    print('inside of action')

    if request.method == 'POST':
        order_id = request.POST['order_id']
        requested_order = Order.objects.get(pk = order_id)
        action = request.POST['action']

        if action == 'completed':
            receiving_otp = random.randint(1000, 9999)
            sender_mail = settings.EMAIL_HOST_USER
            receiver_mail = [requested_order.user.email,]
            subject = f"Your order is prepared!"
            message = f" order id: {order_id} \n Receiving OTP: {receiving_otp} \n Amount: {requested_order.total_price}"
            send_mail(subject, message, sender_mail, receiver_mail)

            requested_order.status = 'completed'
            requested_order.otp = receiving_otp

        elif action == 'cancel':
            requested_order.status = 'canceled'

        requested_order.save()

        return HttpResponse("action " + action + ' performed')

        #page = request.POST['page']

        #if page == 'order':
        #    return redirect(order)

        #return redirect(manage_order, order_type = 'ordered')

def submit_review(request):
    if request.method == 'POST':
        review = request.POST['review']
        Review.objects.create(user = request.user, review = review)

        #make a new review object with arguments review and user

        return HttpResponse('Review Submitted successfully')
