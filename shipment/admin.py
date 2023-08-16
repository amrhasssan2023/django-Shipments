from django.contrib import admin
from .models import Courier, ShipemtTrak, ShipmentStatus, Shipment

# Register your models here.

admin.site.register(Courier)
admin.site.register(ShipemtTrak)
admin.site.register(ShipmentStatus)
admin.site.register(Shipment)

admin.site.site_header = 'Shipment Admin Panal'
admin.site.site_title = 'Shipment Admin Panal'