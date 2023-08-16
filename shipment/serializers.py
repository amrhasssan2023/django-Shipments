from rest_framework import serializers
from .models import Courier, ShipemtTrak, ShipmentStatus, Shipment


class CourierSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'


class ShipemtTrakSerialzer(serializers.ModelSerializer):
    class Meta:
        model = ShipemtTrak
        fields = '__all__'


class ShipmentStatusSerialzer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentStatus
        fields = '__all__'


class ShipmentSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'