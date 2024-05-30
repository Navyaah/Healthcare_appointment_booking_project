
# Create your models here.

from django.db import models

class CustomUser(models.Model):
    is_provider = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username