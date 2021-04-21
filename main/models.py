from django.db import models

class Motorcycle(models.Model):
    name = models.CharField(max_length=100)
    year = models.DecimalField(max_digits=10, decimal_places=0)
    size = models.CharField(max_length=100)
    image = models.ImageField(upload_to='motorcycle_images', default='media/default.png')

    def __str__(self):
        return self.name