from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    balance = models.DecimalField(max_digits=9999999, decimal_places=2)
    inn = models.IntegerField()
