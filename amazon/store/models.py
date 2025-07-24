from django.db import models

# Create your models here.
class Shop(models.Model):
    owner = models.ForeignKey('User', on_delete=models.CASCADE, related_name='owned_shops')

    @property
    def products(self):
        return Product.objects.filter(shop=self)

class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')

    @property
    def reviews(self):
        return Review.objects.filter(product=self)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='reviews')

class User(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='workers', null=True, blank=True)

    @property
    def reviewed_products(self):
        return Review.objects.filter(user=self)
