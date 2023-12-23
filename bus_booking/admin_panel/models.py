from django.db import models


class Adminsingup(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.TextField()
    password = models.CharField(max_length=255)


class Bus_details(models.Model):
    busname = models.CharField(max_length=50)
    busnumber = models.CharField(max_length=50)
    date = models.DateField()
    ticketprice = models.CharField(max_length=50, blank=True, null=True)
    source = models.CharField(max_length=50)
    deparchertime = models.TimeField()
    destination = models.CharField(max_length=50)
    arrivaltime = models.TimeField()
    durition = models.CharField(max_length=50, blank=True, null=True)
    seats = models.CharField(max_length=50)
    availableseats = models.CharField(max_length=50, blank=True, null=True)
    busimg = models.FileField(upload_to='busimages/')


class Booking(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    transactionid = models.CharField(max_length=50)
    noseats = models.CharField(max_length=50)
    totalprice = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    busname = models.CharField(max_length=50, blank=True, null=True)
    busnumber = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    source = models.CharField(max_length=50, blank=True, null=True)
    deparchertime = models.TimeField(blank=True, null=True)
    destination = models.CharField(max_length=50, blank=True, null=True)
    arrivaltime = models.TimeField(blank=True, null=True)
    durition = models.CharField(max_length=50, blank=True, null=True)
