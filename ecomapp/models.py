from django.db import models
from datetime import datetime
from django.urls import reverse


class Listing(models.Model):
    title = models.CharField(max_length=200)
    seller_name = models.CharField(max_length=200, db_index=True)
    city = models.CharField(max_length=100)
    closest_landmark = models.CharField(max_length=50)
    description = models.TextField(blank=True) #Optional description, no max length
    price = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/') #Save inside media folder under date structure
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) #Optional extra photos
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    available = models.BooleanField(default=True)

    def __str__(self): #Show title as the identifier
        return self.title