from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name=("Product Name"))
    description = models.TextField(verbose_name=("Product Description"))
    model = models.CharField(max_length=30, verbose_name=("Product Model"))
    price = models.DecimalField(decimal_places=2, max_digits=6), verbose_name=("Product Price")
    stock_items = models.IntegerField(verbose_name=("Product Items in Stock"))
    BID = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name=("Brand ID"))

class ProductPicture(models.Model):
    PID = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=("Product ID"))
    front_view = models.ImageField(verbose_name=("Product Front Image"))
    top_view = models.ImageField(verbose_name=("Product Top Image"))
    side_view = models.ImageField(verbose_name=("Product Side Image"))
    inner_view = models.ImageField(verbose_name=("Product Inner Image"))

class ProductComment(models.Model):
    PID = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=("Product ID"))
    UID = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=("User ID"))
    comment = models.TextField(verbose_name=("Product Comment"))
    review = models.DecimalField(decimal_places=1,max_digits=2, verbose_name=("Product Stars Review"))
