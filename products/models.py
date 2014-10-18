from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    colors = models.IntegerField()
    image = models.ImageField(upload_to = 'static/products/img')
    #thumbnail = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name
