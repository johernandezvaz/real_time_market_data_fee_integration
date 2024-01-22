# market_data/models.py
from django.db import models

class MarketData(models.Model):
    timestamp = models.IntegerField()  # Use IntegerField for the timestamp as an integer
    symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    exchange = models.CharField(max_length=100)
