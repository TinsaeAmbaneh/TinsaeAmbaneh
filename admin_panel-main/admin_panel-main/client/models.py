from django.db import models

# Create your models here.

class Client(models.Model):
    first_name      = models.CharField(max_length=150)
    last_name       = models.CharField(max_length=150)
    email           = models.EmailField(max_length=254, unique=True)
    phone           = models.CharField(max_length=150)
    devive_IP       = models.CharField(max_length=150)

    def __str__(self):
        return self.email