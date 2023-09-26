from django.db import models

# Create your models here.
class Sneaker(models.Model):
    title = models.CharField()
    description = models.CharField()
    price = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.title
    
