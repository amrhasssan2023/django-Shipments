from django.shortcuts import render
from rest_framework import viewsets , status , filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Courier, ShipemtTrak, ShipmentStatus, Shipment
from .serializers import CourierSerialzer , ShipemtTrakSerialzer, ShipmentStatusSerialzer , ShipmentSerialzer
from django.http import HttpResponse

# Create your views here.
class CourierViewsets(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerialzer
    authentication_classes = (TokenAuthentication)
    permission_classes = (IsAuthenticated)

    def update(self, request, *args, **kwargs):
        response = {
            'message' : 'Invalid way to create or update'
         }
        
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {
            'message' : 'Invalid way to create or update'
         }
        
        return Response(response, status=status.HTTP_400_BAD_REQUEST)        


class ShipemtTrakViewsets(viewsets.ModelViewSet):
    queryset = ShipemtTrak.objects.all()
    serializer_class = ShipemtTrakSerialzer
    authentication_classes = (TokenAuthentication)
    permission_classes = (IsAuthenticated)


class ShipmentStatusViewsets(viewsets.ModelViewSet):
    queryset = ShipmentStatus.objects.all()
    serializer_class = ShipmentStatusSerialzer
    authentication_classes = (TokenAuthentication)
    permission_classes = (IsAuthenticated)


class ShipmentViewsets(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerialzer
    authentication_classes = (TokenAuthentication)
    permission_classes = (IsAuthenticated)
    filter_backends = [filters.SearchFilter]
    search_fields = ['shipment_name']

    @action(methods=['POST'], detail=True)
    def create_shipment(self, request, pk=None):
        shipment = Shipment.objects.create(shipment=shipment)
        serialzer = ShipmentSerialzer(data=request.data)
        json = {
            'message' : 'Create a Waybill',
            'resulte' : serialzer.data,
        }
        return Response(json, status=status.HTTP_201_CREATED)
    
    def print_shipment(self, request, format=None):
        report = Shipment.objects.all()
        response = HttpResponse(content_type = 'application/pdf')

        response['Content-Disposition'] = 'attachment; filename="Report.pdf"'

        context = {
            'report' : report
        }

        return (context , response)

    @action(methods=['DELETE'], detail=True)
    def Cancel(self, request, pk=None):
        Shipment.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)
 