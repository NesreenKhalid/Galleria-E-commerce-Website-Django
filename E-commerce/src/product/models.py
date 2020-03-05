from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    model = models.CharField(max_length=30)
    review = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=6)
    #BID = models.ForeignKey(Brand, on_delete=models.CASCADE)

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
