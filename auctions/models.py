from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Product(models.Model):
    #id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    imageURL = models.CharField(max_length=64, null=True, blank=True)
    description = models.CharField(max_length=64)
    minStartBid = models.FloatField(default=0)
    price = models.ForeignKey('Bid', on_delete=models.CASCADE, blank=True, null=True, related_name="UserBid")
    category = models.CharField(max_length=20)
    expiration_date = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    watchlist = models.ManyToManyField(User, blank=True, related_name="productWatchlist")
    closed = models.BooleanField(default=False)


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, blank=True, null=True)
    bid = models.FloatField(default=0)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.bid)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    field = models.CharField(max_length=2048)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, blank=True, null=True, related_name="comment")
    time = models.DateTimeField(auto_now_add=True)