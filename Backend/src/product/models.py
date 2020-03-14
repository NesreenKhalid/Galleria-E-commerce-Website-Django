from django.db import models
# Create your models here.
from user.models import User

#mina start 
class Category(models.Model):
    name=models.CharField(max_length=30,verbose_name=("Name of Category"))
    image= models.ImageField(upload_to='category/',verbose_name=("Image"))
    catParent=models.ForeignKey('self',limit_choices_to={'catParent__isnull':True}, on_delete=models.CASCADE,blank=True,null=True,verbose_name=("Category Parent"))
    def __str__(self):
        return self.name

class Brand(models.Model):
    name=models.CharField(max_length=30,verbose_name=("Name of Brand"))
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name=("Category"))
    def __str__(self):
        return str(self.name)
#mina end
class ProductPicture(models.Model):
    front_view = models.ImageField(verbose_name=("Product Front Image"))
    top_view = models.ImageField(verbose_name=("Product Top Image"))
    side_view = models.ImageField(verbose_name=("Product Side Image"))
    inner_view = models.ImageField(verbose_name=("Product Inner Image"))

class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name=("Product Name"))
    description = models.TextField(verbose_name=("Product Description"))
    model = models.CharField(max_length=30, verbose_name=("Product Model"))
    price = models.DecimalField(decimal_places=2, max_digits=6,verbose_name=("Product Price"))
    stock_items = models.IntegerField(verbose_name=("Product Items in Stock"))
    pictures = models.ForeignKey(ProductPicture, null=True, on_delete=models.CASCADE, verbose_name="Product Pictures")
    BID = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name=("Brand ID"))

    def __str__(self):
        return str(self.name)

class ProductComment(models.Model):
    PID = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=("Product ID"))
    UID = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=("User ID"))
    comment = models.TextField(verbose_name=("Product Comment"))
    review = models.DecimalField(decimal_places=1,max_digits=2, verbose_name=("Product Stars Review"))
