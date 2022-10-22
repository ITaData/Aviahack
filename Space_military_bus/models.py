from django.db import models

class Bus(models.Model):
    bus_id = models.AutoField().primary_key()
    name = models.CharField(max_length=100)
    spaciousness = models.IntegerField()
    def __str__(self):
        return self.name

class Driver(models.Model):
    id_driver = models.AutoField().primary_key()
    working = models.BooleanField()
    time_working = models.TimeField()
    does_order = models.BooleanField()
    count_trip = models.IntegerField()
    trip = models.ForeignKey('Trip', on_delete=models.PROTECT())
    def __str__(self):
        return self.id_driver


class Operator(models.Model):
    operator_id = models.AutoField().primary_key()
    time_task_generation = models.TimeField()
    driver = models.ForeignKey(Driver, on_delete=models.PROTECT())
    def __str__(self):
        return self.operator_id

class Trip (models.Model):
    trip_id = models.AutoField().primary_key()
    driver = models.ForeignKey(Driver, on_delete=models.PROTECT())
    operator = models.ForeignKey(Operator, on_delete=models.PROTECT())
    count_people = models.IntegerField()
    type_bus = models.IntegerField()
    start_point = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_point = models.CharField(max_length=100)
    end_time = models.TimeField()
    managed = models.BooleanField()
    completed = models.BooleanField()

    def __str__(self):
        return self.trip_id











