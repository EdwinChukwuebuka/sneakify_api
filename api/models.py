from django.db import models

# Create your models here.
class Sneaker(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=128)
    price = models.IntegerField()
    image = models.ImageField(upload_to = '', blank=True, null = True)

    def __str__(self):
        return self.title