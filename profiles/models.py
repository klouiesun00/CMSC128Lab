from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True)
    name = models.CharField(max_length=30, null=True)
    birthday = models.DateField(null=True)
    genres = models.CharField(max_length=40, null=True)
    no_of_books = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
