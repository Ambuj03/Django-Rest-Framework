from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null= True)
    price = models.DecimalField(max_digits=10, default=99.99, decimal_places=2)