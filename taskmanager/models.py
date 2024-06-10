# In models.py

from django.db import models

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    coins = models.JSONField(default=None)

    def __str__(self):
        return str(self.job_id)


class Task(models.Model):
    coin_name = models.CharField(max_length=100)
    job_id = models.ForeignKey(Job, related_name='tasks', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=10)
    price_change = models.DecimalField(max_digits=10, decimal_places=2)
    market_cap = models.BigIntegerField()
    market_cap_rank = models.IntegerField()
    volume = models.BigIntegerField()
    volume_rank = models.IntegerField()
    volume_change = models.DecimalField(max_digits=10, decimal_places=2)
    circulating_supply = models.BigIntegerField()
    total_supply = models.BigIntegerField()
    diluted_market_cap = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Add more fields as needed for contracts, official links, socials, etc.

    def __str__(self):
        return f"{self.coin_name} - {self.created_at}"
