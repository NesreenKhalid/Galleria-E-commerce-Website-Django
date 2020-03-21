from django.db import models

from django.db import models
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


#User: ID (auto increment), name, password, email, phone, picture, credit card id last-login, date-joined
class User (models.Model):
    id = models.AutoField(primary_key = True)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    avatar = models.ImageField()

    def __str__(self):
        return self.username

#User Address
class Address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='product ID')
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)

#Wishlist
class Wishlist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user ID')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='product ID')

class Cart(models.Model):
    PID = models.ForeignKey('product.Product', on_delete=models.CASCADE , verbose_name='product ID')
    UID = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user ID')
    quantity = models.IntegerField(default=1)