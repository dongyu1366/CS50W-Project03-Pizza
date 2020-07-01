from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import AddOns, DinnerPlatters, Order, Pasta, Pizza, Product, Salads, Subs, Toppings

# Create your views here.
def index(request):

    context = {
        "regular_pizzas": Pizza.objects.filter(name="Regular Pizza"),
        "sicilian_pizzas": Pizza.objects.filter(name="Sicilian Pizza"),
        "toppings": Toppings.objects.all(),
        "subs": Subs.objects.all(),
        "addons": AddOns.objects.all(),
        "pastas" : Pasta.objects.all(),
        "salads": Salads.objects.all(),
        "dinner_platters": DinnerPlatters.objects.all(),
    }
    return render(request, "orders/index.html", context)

@login_required(login_url='/users/login/')
def add_pizza(request):
    user=request.user
    name = request.POST.get("pizza").split('#')[0]
    flavor = request.POST.get("pizza").split('#')[1]

    toppings_list = []
    for add in request.POST:
        if add.startswith("topping"):
            topping=str(request.POST.get(add))
            toppings_list.append(topping)
    toppings = toppings_list

    size = request.POST.get("price").split('#')[0]
    price = request.POST.get("price").split('#')[1]
    client = f"{user.first_name} {user.last_name}"

    product = Product(name=name, flavor=flavor, extras=toppings, size=size, price=price, client=client, client_id=user.id)
    product.save()
    messages.success(request, f'Add {name}({flavor}) {size} to the cart.')
    return redirect('index')

@login_required(login_url='/users/login/')
def add_sub(request):
    user = request.user
    name = "Sub"
    flavor = request.POST.get("sub")
    size = request.POST.get("price").split('#')[0]
    o_price = request.POST.get("price").split('#')[1]
    client = f"{user.first_name} {user.last_name}"
    addons = request.POST.getlist("addon")

    # Because some subs do not provide both small & large size, make sure the sub exists
    try:
        t_price = float(o_price) + len(addons)*0.5 # if sub do not exits, o_price will be null
        product = Product(name=name, flavor=flavor, extras=addons, size=size, price=t_price, client=client, client_id=user.id)
        product.save()
        messages.success(request, f'Add {name}({flavor}) {size} to the cart.')
    except:
        messages.warning(request, f'Sorry, {name}({flavor}) does not provide {size} size.')

    return redirect('index')

@login_required(login_url='/users/login/')
def add_pasta(request, pasta_id):
    user = request.user
    client = f"{user.first_name} {user.last_name}"

    pasta = Pasta.objects.filter(id=pasta_id)[0]
    name = pasta.name
    flavor = pasta.flavor
    price = pasta.price

    product = Product(name=name, flavor=flavor, extras="", size="", price=price, client=client, client_id=user.id)
    product.save()
    messages.success(request, f'Add {name}({flavor}) to the cart.')

    return redirect('index')


@login_required(login_url='/users/login/')
def add_salad(request, salad_id):
    user = request.user
    client = f"{user.first_name} {user.last_name}"

    salad = Salads.objects.filter(id=salad_id)[0]
    name = salad.name
    flavor = salad.flavor
    price = salad.price

    product = Product(name=name, flavor=flavor, extras="", size="", price=price, client=client, client_id=user.id)
    product.save()
    messages.success(request, f'Add {name}({flavor}) to the cart.')

    return redirect('index')

@login_required(login_url='/users/login/')
def add_platter(request):
    user = request.user
    name = "Dinner Platter"
    flavor = request.POST.get("platter")
    size = request.POST.get("price").split('#')[0]
    price = request.POST.get("price").split('#')[1]
    client = f"{user.first_name} {user.last_name}"

    product = Product(name=name, flavor=flavor, extras="", size=size, price=price, client=client, client_id=user.id)
    product.save()
    messages.success(request, f'Add {name}({flavor}) {size} to the cart.')

    return redirect('index')

@login_required(login_url='/users/login/')
def delete_product(request, product_id):
    product = Product.objects.filter(id=product_id)
    product[0].delete()

    return redirect('cart')

@login_required(login_url='/users/login/')
def show_cart(request):
    user = request.user
    products = Product.objects.filter(client_id=user.id, status=0)

    if products:
        extras_lists=[]
        total_price = 0
        for x in products:
            total_price += x.price
            extras = x.extras[1:-1].split(", ")
            extras_lists.append(extras)
        products_list = zip(products, extras_lists)
    else:
        products_list = []
        total_price = 0

    context = {"products_list":products_list, "total_price":total_price}

    return render(request, "orders/cart.html", context)

@login_required(login_url='/users/login/')
def placeorder(request):
    user = request.user
    client = f"{user.first_name} {user.last_name}"
    products = Product.objects.filter(client_id=user.id, status=0)
    if request.method == "POST":
        if products:

            # Create a new order
            order = Order(client=client, client_id=user.id)
            order.save()

            for product in products:
                product.status = 1
                product.order = order
                product.save()

                order.total_price += product.price
                order.save()

            messages.success(request, "Success, please wait for completed!")
        else:
            pass

    return redirect('cart')

@login_required(login_url='/users/login/')
def orders(request):
    user = request.user
    orders = Order.objects.filter(client_id=user.id).exclude(status=3)

    return render(request, "orders/orders.html", {"orders":orders})

# Display the orders status are completed
@login_required(login_url='/users/login/')
def orders_completed(request):
    user = request.user
    orders = Order.objects.filter(client_id=user.id, status=3)

    return render(request, "orders/orders.html", {"orders":orders})

@login_required(login_url='/users/login/')
def order_detail(request, order_id):
    user = request.user
    products = Product.objects.filter(order=order_id, client_id=user.id).exclude(status=0)

    if products:
        extras_lists=[]
        total_price = 0
        for x in products:
            total_price += x.price
            extras = x.extras[1:-1].split(", ")
            extras_lists.append(extras)
        products_list = zip(products, extras_lists)
    else:
        return redirect("orders")

    context = {"products_list":products_list, "total_price":total_price}

    return render(request, "orders/order.html", context)

@staff_member_required
def manage_orders(request):
    orders = Order.objects.exclude(status=3)

    return render(request, "orders/manage_orders.html", {"orders":orders})

# Display the orders status are completed
@staff_member_required
def manage_orders_completed(request):
    orders = Order.objects.filter(status=3)

    return render(request, "orders/manage_orders.html", {"orders":orders})

@staff_member_required
def change_order_status(request, order_id):
    new_status = int(request.POST.get("status"))
    order = Order.objects.filter(id=order_id)[0]
    order.status = new_status
    order.save()

    return redirect('manage_orders')

@staff_member_required
def manage_order_detail(request, order_id):
    products = Product.objects.filter(order=order_id).exclude(status=0)

    if products:
        extras_lists=[]
        total_price = 0
        for x in products:
            total_price += x.price
            extras = x.extras[1:-1].split(", ")
            extras_lists.append(extras)
        products_list = zip(products, extras_lists)
    else:
        return redirect("manage_orders")

    context = {"products_list":products_list, "total_price":total_price}

    return render(request, "orders/order.html", context)
