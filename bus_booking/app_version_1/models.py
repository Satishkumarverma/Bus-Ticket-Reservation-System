from django.db import models


class signup(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    dob = models.DateField(max_length=255)
    password = models.CharField(max_length=255)
