import json
from .models import*

def cookieCart(request): 
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        #Handle empty cart for guest user
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}    
        print('Cart: ', cart)

        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False }
        cartItems = order['get_cart_items']
        
        for key in cart: 
            try:
                cartItems += cart[key]['quantity']
                product = Product.objects.get(id=key)
                total = product.price * cart[key]['quantity']
                order['get_cart_items'] += cart[key]['quantity']
                order['get_cart_total'] += total

                if product.digital == False:
                    order['shipping'] = True

                item = {
                    'product': {
                        'id': product.id,
                        'name': product.name,
                        'price': product.price,
                        'imageURL': product.imageURL
                    },
                    'quantity': cart[key]['quantity'],
                    'get_total': total
                }
                items.append(item)
            except:
                pass

    return {'items': items, 'order': order, 'cartItems': cartItems} 

def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request) 
        items = cookieData['items']
        order = cookieData['order']
        cartItems = cookieData['cartItems']

    return {'items': items, 'order': order, 'cartItems': cartItems} 
    