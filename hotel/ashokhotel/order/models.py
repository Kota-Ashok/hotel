from django.db import models

# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date = models.DateField( )
    time = models.TimeField()
    party_size = models.IntegerField()


# models.py
from django.db import models

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    items = models.TextField()

    def __str__(self):
        return self.customer_name