from django.db import models


class Menu(models.Model):
    item_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, default='description will be added soon')
    price = models.IntegerField()
    

class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self): 
        return self.first_name