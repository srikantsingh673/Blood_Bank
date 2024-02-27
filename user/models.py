from django.db import models
from django.contrib.auth.models import User

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    added_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=120, null=False, blank=False)
    mobile = models.CharField(max_length=10, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=120, blank=True, null=True, unique=True)
    blood_group = models.CharField(max_length=5, null=False, blank=False)
    age = models.CharField(max_length=3, null=False, blank=False)
    weight = models.FloatField(max_length=3, null=False, blank=False)
    state = models.CharField(max_length=20, null=False, blank=False)
    district = models.CharField(max_length=25, null=False, blank=False)
    city = models.CharField(max_length=25, null=False, blank=False)
    pin = models.CharField(max_length=6, null=False, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
