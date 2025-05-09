from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return f"{self.category_name}"
class Product(models.Model):
    product_name=models.CharField(max_length=1000,null=True,blank=True)
    product_image=models.ImageField(upload_to="product/",null=True,blank=True)
    product_description=models.TextField(max_length=1000,null=True,blank=True)
    product_price=models.DecimalField(max_digits=4,decimal_places=0,null=True,blank=True)
    product_category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,
    blank=True, related_name="products")
    def __str__(self):
        return f"{self.product_name}"
class Contact(models.Model):
    contact_name=models.CharField(max_length=100,null=True,blank=True)
    contact_email=models.EmailField(null=True,blank=True)
    contact_phone=models.CharField(max_length=100,null=True,blank=True)
    contact_subject=models.CharField(max_length=100,null=True,blank=True)
    contact_message=models.TextField(max_length=1000,null=True,blank=True)
    def __str__(self):
        return f"{self.contact_name}"

