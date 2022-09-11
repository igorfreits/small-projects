from django.db import models

# Create your models here.


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=1000)
    types = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name
