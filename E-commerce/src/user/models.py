from django.db import models

from django.db import models
from django.db import models
from django.utils.translation import ugettext_lazy as _


#User: ID (auto increment), name, password, email, phone, picture, credit card id last-login, date-joined
class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100, verbose_name=_("User Name"))
    user_password = models.CharField(max_length=128, verbose_name=_("User Password"))
    user_email = models.EmailField(blank=True, default='', unique=True, verbose_name=_("Email"))
    user_phone = models.CharField(max_length=128, verbose_name=_("User Phone"))
    user_pic = models.ImageField(upload_to = 'user/', verbose_name=_("Profile Picture") )
    user_credit_id = models.CharField(max_length=128, verbose_name=_("Credit Card ID"))
    last_login = models.DateTimeField(blank=True, null=True, verbose_name=_("Last Login"))
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user_name

#User Address
class Address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='product ID')
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)

#Wishlist
class Wishlist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='product ID')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='product ID')

class Cart(models.Model):
    PID = models.ForeignKey('product.Product', on_delete=models.CASCADE , verbose_name='product ID')
    UID = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user ID')
    quantity = models.IntegerField(default=1)