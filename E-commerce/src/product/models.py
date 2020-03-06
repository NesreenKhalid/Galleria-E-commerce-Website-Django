from django.db import models

# Create your models here.

#mina start 
class Category(models.Model):
    CName=models.CharField(max_length=30,verbose_name=("Name of Category"))
    CImage= models.ImageField(upload_to='product/',verbose_name=("Image"))

    def __str__(self):
        return self.CName

class Brand(models.Model):
    BRDName=models.CharField(max_length=30,verbose_name=("Name of Brand"))
    BRDCategoryID = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name=("Category"))

    def __str__(self):
        return str(self.BRDCategoryID)

#mina end

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    model = models.CharField(max_length=30)
    review = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=6)
   # BID = models.ForeignKey(Brand, on_delete=models.CASCADE)

class ProductPicture(models.Model):
    PID = models.ForeignKey(Product, on_delete=models.CASCADE)
    whole_view = models.ImageField()
    top_view = models.ImageField()
    side_view = models.ImageField()
    inner_view = models.ImageField()

class ProductComment(models.Model):
    PID = models.ForeignKey(Product, on_delete=models.CASCADE)
    #UID = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    review = models.DecimalField(decimal_places=1,max_digits=2)







