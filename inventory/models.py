from django.db import models

# Create your models here.

class Inventory(models.Model):
    gtin = models.BigIntegerField(default = 0)
    expiry_date = models.DateField('expiry date')