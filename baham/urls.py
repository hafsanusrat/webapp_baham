from django.urls import path
from . import views


urlpatterns = [
    path('', views.home ,name='home'),
    path('vehicles', views.view_vehicles ,name='viewvehicle'),
    path('addvehicle', views.view_addvehicle ,name='addvehicle'),
    path('vehicles/save', views.save_vehicle ,name='saveveh'),
    path('vehicles/<int:myKey>/delete/', views.delete_vehicle, name='delveh')
]




