from django.db import models

# Create your models here.

class CustomUser(models.Model):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.is_doctor                                                                                                                                                               