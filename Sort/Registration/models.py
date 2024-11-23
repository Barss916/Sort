from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite = models.JSONField()
    image = models.ImageField(upload_to="media/avatar")

    def __str__(self):
        return self.username
