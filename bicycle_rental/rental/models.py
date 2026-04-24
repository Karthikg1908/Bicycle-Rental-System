from django.db import models

class Bicycle(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField()

class Rental(models.Model):
    customer_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    rent_type = models.CharField(max_length=20)
    rented_on = models.DateTimeField(auto_now_add=True)