from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_pizza", views.add_pizza, name="add_pizza"),
    path("add_sub", views.add_sub, name="add_sub"),
    path("add_pasta/<int:pasta_id>", views.add_pasta, name="add_pasta"),
    path("add_salad/<int:salad_id>", views.add_salad, name="add_salad"),
    path("add_paltter", views.add_platter, name="add_platter"),
    path("delete_product/<int:product_id>", views.delete_product, name="delete_product"),
    path("cart", views.show_cart, name="cart"),
    path("placeorder",views.placeorder,name="placeorder"),
    path("orders", views.orders, name="orders"),
    path("orders-completed", views.orders_completed, name="orders_completed"),
    path("order/<int:order_id>", views.order_detail, name="order"),
    path("manage-orders", views.manage_orders, name="manage_orders"),
    path("manage-orders-completed", views.manage_orders_completed, name="manage_orders_completed"),
    path("change-order-status/<int:order_id>", views.change_order_status, name="change_order_status"),
    path("manage-order/<int:order_id>", views.manage_order_detail, name="manage_order_detail")
]
