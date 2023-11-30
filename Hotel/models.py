from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    manager_name = models.CharField(max_length=50)
    manager_phone = models.CharField(max_length=13)
    manager_email = models.EmailField(blank=True)

    def __str__(self):
        return self.name
