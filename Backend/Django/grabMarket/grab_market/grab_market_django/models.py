from django.db import models

# Create your models here.
class Product(models.Model):        
    ImageUrl = models.CharField(max_length=100)
    seller = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    creatAt = models.DateTimeField( auto_now_add=True)
    description = models.TextField(max_length= 100)
    def __str__(self):
        return self.name
