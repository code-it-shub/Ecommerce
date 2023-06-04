from django.db import models
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.utils.translation import gettext as _
import django.utils.timezone



class user(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    phone = models.CharField(max_length=20,unique=True,blank=True,null=True)
    profilepic= models.ImageField(upload_to='userprofile/',blank=True,null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['phone','profilepic',]

    objects = UserManager()
    def __str__(self):
        return f"{self.email}"


    
# Create your models here.
class product_category(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    desc= models.TextField(max_length=100)
    created_at=models.DateTimeField(auto_created=True,null=True,default=django.utils.timezone.now) 

    def __str__(self):
        return f"{self.name}"


class product_inventory(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20,blank=False, default='product_error')
    quantity = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_created=True,null=True,default=django.utils.timezone.now)

    def __str__(self):
        return f"{self.name}"


class discount(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20,null=False)
    desc=models.TextField(max_length=100)
    discount_percentage=models.IntegerField(blank=True)
    active=models.BooleanField()
    created_at=models.DateTimeField(auto_created=True,null=True,default=django.utils.timezone.now)
    
    def __str__(self):
        return f"{self.name}"

class product(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    desc=models.TextField(max_length=100)
    categor_id=models.ForeignKey(product_category,on_delete=models.CASCADE)
    inventory_id=models.ForeignKey(product_inventory,on_delete=models.CASCADE)
    price=models.DecimalField(blank=False,max_digits=10,decimal_places=2)
    discount_id=models.ForeignKey(discount,on_delete=models.CASCADE)
    product_image=models.ImageField(upload_to='media/')

    def __str__(self):
        return f"{self.name}"

# class user(models.Model):
#     id=models.IntegerField(primary_key=True)
#     username = models.CharField(max_length=20, blank=False)
#     password= models.CharField(max_length=50 ,blank=False)
#     first_name=models.CharField(max_length=20, blank=False)
#     last_name=models.CharField(max_length=20)
#     telephone=PhoneNumberField()
#     created_at=models.DateTimeField()

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"


class payment_detial(models.Model):
    PENDING = 0
    DONE = 1
    STATUS_CHOICES = (
    (PENDING, 'Pending'),
    (DONE, 'Done'), 
    )
    id=models.IntegerField(primary_key=True)
    amount=models.FloatField(null=True,default=0)
    order_id=models.IntegerField(null=True,blank=True,unique=True)
    status=models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_at=models.DateTimeField(auto_created=True,null=True,default=django.utils.timezone.now)
 
class order_details(models.Model):
    id=models.IntegerField(primary_key=True)
    user_id=models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)
    total=models.DecimalField(max_digits=10,decimal_places=2)
    payment_id=models.ForeignKey(payment_detial,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_created=True,null=True,default=django.utils.timezone.now)


class shopping_session(models.Model):
    id=models.IntegerField(primary_key=True)
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    total=models.FloatField(null=True)
    created_at=models.DateTimeField(auto_created=True,blank=True,null=True)

class cart_items(models.Model):
    id=models.IntegerField(primary_key=True)
    session_id=models.ForeignKey(shopping_session,on_delete=models.CASCADE,null=True)
    product_id=models.ForeignKey(product,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField(blank=False,null=False,default=0)
    created_at=models.DateTimeField(auto_created=django.utils.timezone.now)


class order_item(models.Model):
    id=models.IntegerField(primary_key=True)
    order_id=models.ForeignKey(order_details,on_delete=models.CASCADE,blank=True,null=True)
    product_id=models.ForeignKey(product,on_delete=models.CASCADE,blank=True,null=True)
    quanity=models.IntegerField(blank=False, default=0)
    created_at=models.DateTimeField(auto_created=True,null=True,default=django.utils.timezone.now)

class user_address(models.Model):
    id=models.IntegerField(primary_key=True)
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    address_line1=models.CharField(max_length=100,null=True,blank=True)
    address_line2=models.CharField(max_length=100,null=True,blank=True)
    city=models.CharField(max_length=20,blank=True, null=True)
    postal_code=models.IntegerField(blank=True,null=True)
    state=models.CharField(max_length=20,blank=True, null=True)
    country=models.CharField(max_length=20,blank=True, null=True)
    phone = models.CharField(max_length=20,unique=True,blank=True,null=True)

class user_payment(models.Model):
    payment_mode = [
        ("O","ONLINE"),
        ("C","CASH"),
    ]
    id=models.IntegerField(primary_key=True) 
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    payment_type=models.CharField(max_length=1, choices=payment_mode)

