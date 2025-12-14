from django.db import models

# Create your models here.


class Program(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.ImageField(upload_to="programs/")
    seats = models.IntegerField(default=30)
    lessons = models.IntegerField(default=40)
    hours = models.IntegerField(default=60)

    def __str__(self):
        return self.title