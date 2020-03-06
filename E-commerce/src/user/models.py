from django.db import models

# Create your models here.

class Cart(models.Model):
    PID = models.ForeignKey('product.Product', on_delete=models.CASCADE , verbose_name='product ID')
    #UID = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user ID')
    quantity = models.IntegerField(default=1)