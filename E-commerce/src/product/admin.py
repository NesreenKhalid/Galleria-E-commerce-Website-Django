from django.contrib import admin

# Register your models here.
from product.models import Product, ProductPicture, ProductComment

admin.site.register(Product)
admin.site.register(ProductPicture)
admin.site.register(ProductComment)