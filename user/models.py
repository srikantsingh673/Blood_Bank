from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    DateTime = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=50, unique=True, null=False)
    state = models.CharField(max_length=50, null=False)
    district = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=50, null=False)
    blood_group = models.CharField(max_length=20, null=False)
    age = models.IntegerField()
    weight = models