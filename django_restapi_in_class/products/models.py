from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField(validators=[MinValueValidator(0)])
    stock = models.IntegerField()
    register_date = models.DateField()