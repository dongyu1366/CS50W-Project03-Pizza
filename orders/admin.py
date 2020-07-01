from django.contrib import admin
from .models import AddOns, DinnerPlatters, Order, Pasta, Pizza, Product, Salads, Subs, Toppings

# Register your models here.
class ProductInline(admin.TabularInline):
    model = Product

class OrderAdmin(admin.ModelAdmin):

    #  Order is able to show and edit its products in admin
    inlines = [ProductInline,]

    list_display = ('id', 'client', 'total_price', 'status',)
    list_editable = ('status',)
    list_filter = ('status',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'name', 'status',)

class SubsAdmin(admin.ModelAdmin):

    list_display = ('flavor', 'small_price', 'large_price',)
    list_editable = ('small_price', 'large_price',)

admin.site.register(AddOns)
admin.site.register(DinnerPlatters)
admin.site.register(Order, OrderAdmin)
admin.site.register(Pasta)
admin.site.register(Pizza)
admin.site.register(Product, ProductAdmin)
admin.site.register(Salads)
admin.site.register(Subs, SubsAdmin)
admin.site.register(Toppings)
