from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.CharField(max_length=2000)

    def __str__(self):
        return f"{self.name} - {self.price}"
