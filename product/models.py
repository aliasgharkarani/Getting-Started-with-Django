from django.db import models

# Create your models here.
class product(models.Model):
    title=models.TextField()
    price=models.TextField()
    quantity=models.TextField()
