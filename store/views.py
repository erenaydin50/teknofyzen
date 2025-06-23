from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Product, Order, Category


def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})


def contact_view(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        success = True
    return render(request, 'store/contact.html', {'success': success})


def dashboard(request):
    return render(request, 'store/dashboard.html')


@login_required(login_url='/accounts/login/')
def orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'store/orders.html', {'orders': orders})


def product_list(request):
    best_sellers = Product.objects.filter(is_best_seller=True)[:3]
    return render(request, 'store/product_list.html', {'best_sellers': best_sellers})


@login_required(login_url='/accounts/login/')
def satın_al(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/satın_al.html', {'product': product})


@login_required(login_url='/accounts/login/')
def odeme(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order_confirmed = False
    if request.method == 'POST':
        Order.objects.create(user=request.user, product=product)
        order_confirmed = True
    return render(request, 'store/storeodeme.html', {
        'product': product,
        'order_confirmed': order_confirmed
    })


def payment_success(request):
    return render(request, 'store/payment_success.html')


@login_required(login_url='/accounts/login/')
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('view_cart')


@login_required(login_url='/accounts/login/')
def view_cart(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        product.quantity = quantity
        product.total_price = product.price * quantity
        products.append(product)
        total += product.total_price
    return render(request, 'store/cart.html', {'products': products, 'total': total})


@login_required(login_url='/accounts/login/')
@csrf_exempt
def checkout(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        product.quantity = quantity
        product.total_price = product.price * quantity
        products.append(product)
        total += product.total_price

    if request.method == 'POST':
        for product in products:
            Order.objects.create(user=request.user, product=product)
        request.session['cart'] = {}
        return redirect('thank_you')

    return render(request, 'store/checkout.html', {'products': products, 'total': total})


@login_required(login_url='/accounts/login/')
def thank_you(request):
    return render(request, 'store/thank_you.html')


@login_required(login_url='/accounts/login/')
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('view_cart')


# ✅ Satıştakiler Sayfası
def for_sale(request, category_id=None):
    categories = Category.objects.all()
    if category_id:
        sale_products = Product.objects.filter(category_id=category_id)
    else:
        sale_products = Product.objects.all()

    return render(request, 'store/for_sale.html', {
        'products': sale_products,
        'categories': categories,
        'selected_category': category_id
    })