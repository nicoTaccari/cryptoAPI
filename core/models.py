from django.db import models

# Create your models here.


class Coin(models.Model):
    ticker = models.CharField(max_length=15)


class Coin_Price(models.Model):
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    open = models.CharField(max_length=50)
    high = models.CharField(max_length=50)
    low = models.CharField(max_length=50)
    close = models.CharField(max_length=50)
