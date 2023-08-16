from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_measurement.models import MeasurementField
from measurement.measures import Volume, Distance, Area , Weight
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.

class Courier(models.Model):
    Courier_status = [
        ('Available','Available'),
        ('Unavailable','Unavailable'),
    ]
    name = models.CharField(max_length=250)
    decription = models.TextField(max_length=500, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    courier_status = models.CharField(max_length=150, choices=Courier_status, null=True, blank=True)
    client_id =  models.IntegerField(null=True, blank=True)
    client_name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name
    
class ShipemtTrak(models.Model):
    courier = models.ForeignKey(Courier,related_name='shipment', on_delete=models.CASCADE)
    trak = models.CharField(max_length=120)

    def __str__(self):
        return self.trak
    
class ShipmentStatus(models.Model):
    SHIPMENT_STATUS = [
        ('Proccessing','Proccessing'),
        ('Confirmed','Confirmed'),
        ('Deliverd','Deliverd'),
        ('Canceled','Canceled'),
    ] 

    shipment_status = models.CharField(max_length=250, choices=SHIPMENT_STATUS)
    decription = models.TextField(max_length=500, null=True, blank=True)


    def __str__(self):
        return self.shipment_status

class Shipment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, related_name='courier',on_delete=models.CASCADE)
    shipment_name = models.CharField(max_length=150)
    shimpemt_trak = models.ForeignKey(ShipemtTrak, on_delete=models.CASCADE)
    shimpemt_status = models.ForeignKey(ShipmentStatus, on_delete=models.CASCADE)
    sender_address = models.TextField(max_length=500,null=True, blank=True)
    sender_country = CountryField(null=True, blank=True)
    sender_phone_number = PhoneNumberField(null=True, blank=True)
    receiver_address = models.TextField(max_length=500)
    receiver_country = CountryField(null=True, blank=True)
    receiver_phone_number = PhoneNumberField(null=True, blank=True)
    shipment_Content = models.TextField(max_length=150)
    number_of_pieces = models.IntegerField()
    volume = str(MeasurementField(measurement=Volume))
    sides = str(MeasurementField(measurement=Distance))
    material_size = str(MeasurementField(measurement=Area))
    max_weight = str(MeasurementField(measurement=Weight))

    
    def __str__(self):
        return self.shipment_name
