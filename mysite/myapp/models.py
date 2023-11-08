from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.urls import reverse


class Product(models.Model):

    # user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.CharField(max_length=2000)
    image = models.ImageField(blank=True, upload_to='images/products')

    def __str__(self):
        return f"{self.name} - {self.price}"

    def get_absolute_url(self):
        return reverse("myapp:productsl")
