from django.urls import path , include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('courier', views.CourierViewsets)
router.register('trak', views.ShipemtTrakViewsets)
router.register('status', views.ShipmentStatusViewsets)
router.register('Shipment', views.ShipmentViewsets)

urlpatterns = [
    path('api-auth', include('rest_framework.urls')),
    path('api/viewsets/', include(router.urls)),

]