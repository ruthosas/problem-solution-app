from django.contrib.auth.models import User
from django.db import models

class Unit(models.Model):
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.unit

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    unit_head = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user)