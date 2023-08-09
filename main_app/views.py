import stripe
import json
from django.shortcuts import get_object_or_404
from django.views import View
from django.conf import settings
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, Order, OrderItem, Review, User

from .forms import UserForm
from .forms import ReviewForm


stripe.api_key = settings.STRIPE_API_KEY_HIDDEN

YOUR_DOMAIN = 'http://localhost:8000'

# Create your views here.


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {
        'products': products
    })


def learn(request):
    return render(request, 'learn.html')


def products_index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {
        'products': products
    })


def products_detail(request, product_id):
    product = Product.objects.get(id=product_id)

    review_form = None

    if request.user.is_authenticated:
        user = request.user
        delivered_orders = Order.objects.filter(
            user=user, status='D', orderitem__product=product)

        if delivered_orders.exists():
            review_form = ReviewForm()

    reviews_for_product = product.reviews.all()

    return render(request, 'products/detail.html', {
        'product': product,
        'review_form': review_form,
        'reviews': reviews_for_product
    })


def add_review(request, product_id):
    form = ReviewForm(request.POST)

    if form.is_valid():
        product = Product.objects.get(id=product_id)
        # user = User.objects.get(id=user_id)
        user_id = request.user.id

        new_review = form.save(commit=False)
        new_review.product = product
        new_review.user_id = user_id
        new_review.save()

    return redirect('detail', product_id)


# def edit_review(request, review_id, product_id):
#     review = Review.objects.get(id=review_id)
#     # form = ReviewForm(request.POST)

#     if request.method == 'POST':
#         new_content = request.POST.get('content')
#         review.content = new_content
#         review.save()
#         return redirect('detail', product_id=review.product.id)

#     return render(request, 'product_detail.html', {'product': review.product, 'edit_review_id': review.id})


def delete_review(request, product_id):
    if request.method == 'POST':
        review_id = request.POST.get('review_id')
        print("Review ID:", review_id)
        print("Product ID:", product_id)
        try:
            review = Review.objects.get(id=review_id, product_id=product_id)
            print("Review found:", review)
            review.delete()
        except Review.DoesNotExist:
            print("Review not found")
        return redirect('detail', product_id=product_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def cart(request):
    # If user is authenticated, get their cart
    if request.user.is_authenticated:
        cart = Order.objects.filter(user=request.user, status='C').last()
    # If not, fetch the cart from the session
    else:
        cart_id = request.session.get('cart_id')
        cart = Order.objects.filter(
            id=cart_id, status='C').last() if cart_id else None

    return render(request, 'cart.html', {'cart': cart}) #there MIGHT BE A PROBLEM HERE MEANING ONCE GUESTS CHECKOUT THEY CAN NO LONGER ADD TO CART


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    quantity = int(request.POST.get('quantity', 1))

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(
            user=request.user, status='C')
    else:
        order_id = request.session.get('cart_id')
        if order_id:
            order = Order.objects.get(id=order_id, status='C')
        else:
            order = Order.objects.create(status='C')
            request.session['cart_id'] = order.id

    # Check if the product already exists in the cart based solely on the product and order
    order_item, item_created = OrderItem.objects.get_or_create(product=product, order=order)

    # Update the quantity of the product in the cart
    if item_created:
        order_item.quantity = quantity
    else:
        order_item.quantity += quantity

    order_item.save()

    messages.success(request, "Item added to cart successfully!")
    return redirect('detail', product_id=product_id)


def update_cart(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))

        if request.user.is_authenticated:
            cart = Order.objects.filter(user=request.user, status='C').last()
        else:
            cart_id = request.session.get('cart_id')
            cart = Order.objects.filter(
                id=cart_id, status='C').last() if cart_id else None

        if not cart:
            messages.warning(request, "No active cart found!")
            return redirect('cart')

        order_item = OrderItem.objects.filter(
            product_id=product_id, order=cart).first()

        if order_item:
            order_item.quantity = quantity
            order_item.save()
            messages.success(request, "Item quantity updated successfully!")
        else:
            messages.warning(request, "Item not found in the cart!")

    return redirect('cart')


def remove_from_cart(request, product_id):
    if request.user.is_authenticated:
        cart = Order.objects.filter(user=request.user, status='C').last()
    else:
        # Handle guest users by fetching the cart from the session
        cart_id = request.session.get('cart_id')
        cart = Order.objects.filter(
            id=cart_id, status='C').last() if cart_id else None

    if not cart:
        messages.warning(request, "No active cart found!")
        return redirect('cart')

    order_item = OrderItem.objects.filter(
        product_id=product_id, order=cart).first()
    if order_item:
        order_item.delete()
        messages.success(request, "Item removed from cart successfully!")
    else:
        messages.warning(request, "Item not found in the cart!")

    return redirect('cart')


def checkout(request):
    pub_key = 'pk_test_51NcAplKTTNpybu1oBa9m6XeqC3TGQOCw0EYJQhJJHLCf3eC996sIC8pdtr7NSw3GBDYpPZdEEJIA4TW7FYZDvCD200HwjTkail'
    print('Hello')
    print(pub_key)
    cart = Order.objects.filter(user=request.user, status='C').last()
    cart.save()
    return render(request, 'checkout.html', {'cart': cart, 'pub_key': pub_key})



class CreateCheckoutSessionView(View): 
    def post(self, request, *args, **kwargs):
        # For logged-in users, fetch their cart
        if request.user.is_authenticated:
            cart = Order.objects.filter(user=request.user, status='C').last()
        # For guests, fetch the cart from the session
        else:
            cart_id = request.session.get('cart_id')
            cart = Order.objects.filter(id=cart_id, status='C').last()

        # If no cart is found (neither for logged-in users nor for guests)
        if not cart:
            return HttpResponseBadRequest("No active cart found")

        line_items = []
        for item in cart.orderitem_set.all():
            line_items.append({
                'price_data': {
                    'currency': 'usd',
                    # Stripe expects amounts in cents
                    'unit_amount': int(item.product.price * 100),
                    'product_data': {
                        'name': item.product.name,
                        # Add images if you have
                    },
                },
                'quantity': item.quantity,
            })

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=YOUR_DOMAIN +
            '/success/?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=YOUR_DOMAIN + '/cancel/',
            shipping_address_collection={'allowed_countries': ['US', 'CA'], },
        )

        checkout_session.success_url = checkout_session.success_url.replace(
            '{CHECKOUT_SESSION_ID}', checkout_session.id)

        cart.session_id = checkout_session.id
        cart.save()

        return JsonResponse({
            'id': checkout_session.id
        })



def checkout_success(request):
    session_id = request.GET.get('session_id')
    print("Extracted session_id:", session_id)

    session = stripe.checkout.Session.retrieve(session_id)

    try:
        order = Order.objects.get(session_id=session_id)
    except Order.DoesNotExist:
        print(f"No Order found for session_id: {session_id}")
        order = None

    if session.payment_status == 'paid':
        order.status = 'P'
        order.save()

    return render(request, 'success.html')


def checkout_cancel(request):
    return render(request, 'cancel.html')


@login_required
def account_view(request):
    user_orders = Order.objects.filter(user=request.user)
    if request.method == 'POST':
        # Handle user profile update here
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('account')
    else:
        user_form = UserForm(instance=request.user)
    return render(request, 'account.html', {'orders': user_orders, 'user_form': user_form})


def order_detail_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_detail.html', {'order': order})


def logout_view(request):
    logout(request)
    return redirect('/')
