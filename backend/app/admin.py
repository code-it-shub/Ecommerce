from django.contrib import admin
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Register your models here.

admin.site.register(models.product_category)
admin.site.register(models.product_inventory)
admin.site.register(models.discount)
admin.site.register(models.product)
admin.site.register(models.order_details)
admin.site.register(models.order_item)
admin.site.register(User)
admin.site.register(models.user_payment)
admin.site.register(models.user_address)
admin.site.register(models.cart_items)
admin.site.register(models.payment_detial)