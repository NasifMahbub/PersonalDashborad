# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser, models.Model):
    pass
    # add additional fields in here
    contact_no = models.CharField(max_length=20, default = "")
    def __str__(self):
        return self.username