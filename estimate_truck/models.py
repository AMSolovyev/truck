from django.db import models


class TruckModel(models.Model):
    model_name = models.CharField(max_length=20)
    max_weight = models.PositiveSmallIntegerField(default=100)

    def __str__(self):
        return self.model_name


class Truck(models.Model):
    onboard_number = models.CharField(max_length=20)
    truck_model = models.ForeignKey(TruckModel, on_delete=models.CASCADE)
    current_weight = models.PositiveSmallIntegerField(default=0)

    @property
    def overload(self):
        max_weight = self.truck_model.max_weight
        current_weight = self.current_weight

        if current_weight > max_weight:
            return round((((current_weight - max_weight)/max_weight)*100), 1)
        else:
            return None

    def __str__(self):
    	return self.onboard_number
