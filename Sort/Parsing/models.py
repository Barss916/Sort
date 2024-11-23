from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/shops")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    availability = models.BooleanField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to="media/products")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.name