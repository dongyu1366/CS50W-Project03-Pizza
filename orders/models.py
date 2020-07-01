from django.db import models
from decimal import Decimal

# Create your models here.
class Pizza(models.Model):
    """
    The model holds all common fields of a pizza
    """
    NAME_CHOICE = [
        ("Regular Pizza", "Regular Pizza"),
        ("Sicilian Pizza", "Sicilian Pizza"),
    ]

    FLAVOR_CHOICES = [
        ("", "Cheese"),
        ("1", "1 topping"),
        ("12", "2 toppings"),
        ("123", "3 toppings"),
        ("1234", "Special")
    ]

    name = models.CharField(max_length=60, choices=NAME_CHOICE)
    flavor = models.CharField(max_length=60, choices=FLAVOR_CHOICES, blank=True)
    small_price = models.DecimalField(max_digits=5, decimal_places=2)
    large_price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = "1. Pizza"

    def __str__(self):
        return f'{self.name} - Flavor: {self.get_flavor_display()}'

class Toppings(models.Model):
    """
    The model holds all toppings for a pizza
    """
    name = models.CharField(max_length=60)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = "2. Toppings"

    def __str__(self):
        return self.name

class Subs(models.Model):
    """
    The model holds all common fields of a sub
    """

    name = "Sub"
    flavor = models.CharField(max_length=60)
    small_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    large_price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = "3. Subs"

    def __str__(self):
        return f'{self.name} - {self.flavor}'

class AddOns(models.Model):
    """
    The model holds all add-ons for a sub
    """

    name = models.CharField(max_length=60)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = "4. Add-ons"

    def __str__(self):
        return self.name

class Pasta(models.Model):
    """
    The model holds all common fields of a pasta
    """

    name = "Pasta"
    flavor = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = "5. Pasta"

    def __str__(self):
        return f'{self.name} - {self.flavor}'

class Salads(models.Model):
    """
    The model holds all common fields of a salad
    """
    name = "Salad"
    flavor = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = "6. Salads"

    def __str__(self):
        return f'{self.name} - {self.flavor}'

class DinnerPlatters(models.Model):
    """
    The model holds all common fields of a dinner platter
    """

    name = "Dinner Platter"
    flavor = models.CharField(max_length=60)
    small_price = models.DecimalField(max_digits=5, decimal_places=2)
    large_price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = "7. Dinner platters"

    def __str__(self):
        return f'{self.name} - {self.flavor}'

class Order(models.Model):
    """
    The model holds all common fields of a order
    """

    STATUS_CHOICES = [
        (0, "Pending"),
        (1, "Preparing"),
        (2, "Delivered"),
        (3, "Completed")
    ]

    client = models.CharField(max_length=60)
    client_id = models.IntegerField()
    total_price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    time = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    class Meta:
        verbose_name_plural = "9. Orders"

    def __str__(self):
        return f"{self.id}. Client:{self.client}--({self.get_status_display()})"

class Product(models.Model):
    """
    The model holds all common fields of product, be created when a user add a product into the cart
    """

    STATUS_CHOICES = [
        (0, "In Cart"),
        (1, "In order"),
    ]
    name = models.CharField(max_length=60)
    flavor = models.CharField(max_length=60)
    extras = models.CharField(max_length=60)
    size = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    client = models.CharField(max_length=60)
    client_id = models.IntegerField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    order = models.ForeignKey("order", on_delete=models.CASCADE, blank=True, null=True, related_name="product")

    class Meta:
        verbose_name_plural = "8. Products"

    def __str__(self):
        return f'{self.id}. {self.client} - {self.name}-{self.flavor} - Status: {self.get_status_display()} '
