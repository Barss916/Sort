from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/shops")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    availability = models.BooleanField()
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="media/products")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.name