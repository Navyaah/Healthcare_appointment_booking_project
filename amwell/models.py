
# Create your models here.

from django.db import models

class CustomUser(models.Model):
    is_provider = models.TextField(max_length=100)
    is_patient = models.TextField(max_length=130)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.is_patient