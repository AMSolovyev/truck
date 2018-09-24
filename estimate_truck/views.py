from django.shortcuts import render
from .models import Truck, TruckModel


def trucks_table(request):
    truck_select = request.POST.get('truck_select')
    truck_models = TruckModel.objects.all()

    if (truck_select is None or truck_select == 'all'):
        trucks = Truck.objects.all().order_by('onboard_number')
    else:
        trucks = Truck.objects.filter(truck_model=truck_select).all()

    return render(request, 'estimate_truck/trucks_table.html', {'trucks': trucks,
                                                       'truck_models': truck_models
                                                       })
