from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json

# Create your views here.
def store(request):
    context = obtener_orden_y_items(request)
    products = Product.objects.all()
    context["products"] = products
    return render(request, 'store/store.html', context)

def cart(request):
    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     order, created = Order.objects.get_or_create(
    #         customer = customer,
    #         complete = False
    #     )
    #     items = order.orderitem_set.all()
    # else:
    #     items = []
    #     order = {'get_cart_total': 0, 'get_cart_items' : 0}
    # context = {
    #     'items':items,
    #     'order':order
    # }
    context = obtener_orden_y_items(request)
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = obtener_orden_y_items(request)
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    producId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=producId)
    order,_=Order.objects.get_or_create(
        customer =customer,
        complete=False
    )
    orderItem, _ = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem -= 1
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse(
        'Item was added',
        safe=False
    )
    


def obtener_orden_y_items(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer = customer,
            complete = False
        )
        items = order.orderitem_set.all()
        cartItems = order["get_cart_items"]
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items' : 0}
    context = {
        'items':items,
        'order':order,
        'cartItems': cartItems
    }
    return context
