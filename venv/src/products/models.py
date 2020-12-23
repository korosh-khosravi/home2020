from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=4, max_digits=10000)
    summery = models.TextField(blank=False, null=False)
    feature = models.BooleanField()

