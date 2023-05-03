from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.template import loader
from baham.models import VehicleModel
from django.urls import reverse
from django.shortcuts import get_object_or_404


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))



def view_vehicles(request):
    template = loader.get_template('vehicles.html')
    veh = VehicleModel.objects.all()
    context = {
        "vehicles": veh
    }
    return HttpResponse(template.render(context, request))

def view_addvehicle(request):
    template = loader.get_template('addvehicle.html')
    return HttpResponse(template.render({}, request))

def save_vehicle(request):
    _vendor = request.POST.get('vendor')
    _model = request.POST.get('model')
    _type = request.POST.get('type')
    _capacity = request.POST.get('capacity')

    newVeh = VehicleModel(vendor=_vendor, model=_model, type=_type, capacity=_capacity)
    newVeh.save()

    return HttpResponseRedirect(reverse('viewvehicle'))

def delete_vehicle(request, myKey):
    vehicle = get_object_or_404(VehicleModel, pk=myKey)
    vehicle.delete()
    return HttpResponseRedirect('viewvehicle')
