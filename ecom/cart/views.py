from django.shortcuts import render, get_object_or_404

from store.views import product
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages

def cart_summary(request):
    return render(request, "cart_summary.html", {})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        product = get_object_or_404(Product, id=product_id)

        cart.add(product=product)

        cart_quantity = cart.__len__()

        response = JsonResponse({'qty: ': cart_quantity})
        messages.success(request, ("Product Added To Cart..."))
        return response


def cart_remove(request):
    pass

def cart_update(request):
    pass
