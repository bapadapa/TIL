from django.db import models

# Create your models here.
class Message(models.Model):
    message = models.CharField(max_length=30)
    sub_time = models.TimeField(auto_now_add=True)
    update_time = models.TimeField(auto_now=True)
