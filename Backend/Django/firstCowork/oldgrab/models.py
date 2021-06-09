from django.db import models

# Create your models here.
class Products(models.Model):
    s_id = models.IntegerField(default = 0)
    s_name =models.CharField(max_length=30)
    s_price =  models.IntegerField(default = 0)
    s_seller  =models.CharField(max_length=30)
    s_imageUrl =models.CharField(max_length=100)
    s_description =models.CharField(max_length=100)