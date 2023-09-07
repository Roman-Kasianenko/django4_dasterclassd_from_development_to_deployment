from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile.jpg', upload_to='profile_pictures')
    contact_number = models.CharField(max_length=50, default='0000000')

    def __str__(self):
        return f'Profile - {self.user.username}'
