from decimal import Decimal

from django.db.models import Sum
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db import models, transaction
from django.contrib.auth.models import User


# Create your models here.


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f""" user:{self.user} time:{self.time} """

    @staticmethod
    def get_balance(user: User):
        amount = Payment.objects.filter(user=user).aggregate(Sum('amount'))['amount_sum']
        return amount or Decimal(0)


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='product_name')
    product_id = models.CharField(max_length=255, verbose_name='product_id')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image_url = models.URLField(blank=True, null=True)
<<<<<<< HEAD
=======
    image = models.ImageField(upload_to='images/', blank=True, null=True)
>>>>>>> 800faf1 (Initial commit)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['pk']

    def __str__(self):
<<<<<<< HEAD
        return f""" product:{self.name}\nprice:{self.price} """
=======
        return f""" product:{self.name} """
>>>>>>> 800faf1 (Initial commit)


class Order(models.Model):
    STATUS_CART = '1cart'
    STATUS_WAIT = '2wait'
    STATUS_PAID = '3paid'
    STATUS_CHOICES = [(STATUS_CART, 'cart'),
                      (STATUS_WAIT, 'wait'),
                      (STATUS_PAID, 'paid')]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS_CART)
    amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    payment = models.ForeignKey(Payment, on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f""" user:{self.user} status:{self.status} """

    @staticmethod
    def get_cart(user: User):
        cart = Order.objects.filter(user=user, status=Order.STATUS_CART).first()

        # if cart and (timezone.now() - cart.creation_time).days > 7:
        #     cart.delete()
        #     cart = None

        if not cart:
            cart = Order.objects.create(user=user, status=Order.STATUS_CART, amount=0)

        return cart

    def get_amount(self):
        amount = Decimal(0)
        for item in self.orderitem_set.all():
            amount += item.amount
        return amount

    def make_order(self):
        items = self.orderitem_set.all()
        if items and self.status == Order.STATUS_CART:
            self.status = Order.STATUS_WAIT
            self.save()
<<<<<<< HEAD
            auto_payment_unpaid_order(self.user)
=======
            # auto_payment_unpaid_order(self.user)
>>>>>>> 800faf1 (Initial commit)

    @staticmethod
    def get_amount_of_unpaid_orders(user: User):
        amount = Order.objects.filter(user=user,
                                      status=Order.STATUS_WAIT,
                                      ).aggregate(Sum('amount'))['amount_sum']
        return amount or Decimal(0)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    discount = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f""" product:{self.product}\nprice:{self.price} """

    @property
    def amount(self):
        return self.quantity * (self.price - self.discount)


<<<<<<< HEAD
@transaction.atomic()
def auto_payment_unpaid_order(user: User):
    unpaid_orders = Order.objects.filter(user=user, status=Order.STATUS_WAIT)

    for order in unpaid_orders:
        if Payment.get_balance(user) < order.amount:
            break
        order.payment = Payment.objects.all().last()
        order.status = Order.STATUS_PAID
        order.save()
        Payment.objects.create(user=user, amount=-order.amount)
=======
# @transaction.atomic()
# def auto_payment_unpaid_order(user: User):
#     unpaid_orders = Order.objects.filter(user=user, status=Order.STATUS_WAIT)
#
#     for order in unpaid_orders:
#         if Payment.get_balance(user) < order.amount:
#             break
#         order.payment = Payment.objects.all().last()
#         order.status = Order.STATUS_PAID
#         order.save()
#         Payment.objects.create(user=user, amount=-order.amount)
>>>>>>> 800faf1 (Initial commit)


@receiver(post_save, sender=OrderItem)
def rec_order_amount_save(sender, instance, **kwargs):
    order = instance.order
    order.amount = order.get_amount()
    order.save()


@receiver(post_delete, sender=OrderItem)
def rec_order_amount_delete(sender, instance, **kwargs):
    order = instance.order
    order.amount = order.get_amount()
    order.save()


<<<<<<< HEAD
@receiver(post_save, sender=Payment)
def auto_payment(sender, instanse, **kwargs):
    user = instanse.order
    auto_payment_unpaid_order(user)
=======
# @receiver(post_save, sender=Payment)
# def auto_payment(sender, instance, **kwargs):
#     user = instance.order
#     auto_payment_unpaid_order(user)
>>>>>>> 800faf1 (Initial commit)
