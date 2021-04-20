from django.db import models

class Motorcycle(models.Model):
    name = models.CharField(max_length=100)
    year = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=100)
    img_url = models.CharField(max_length=100)

    def __str__(self):
        return self.name