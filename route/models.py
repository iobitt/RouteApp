import datetime

from django.db import models
from django.contrib.auth.models import User


class Route(models.Model):
    """ Маршрут """

    # Название
    name = models.CharField(max_length=60, unique=True)
    # Владелец
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # Дата начала поездки
    start_date = models.DateField(null=True)
    # Дата окончания поездки
    end_date = models.DateField(null=True)


class Waypoint(models.Model):
    """ Точка маршрута """

    # Название
    name = models.CharField(max_length=60)
    # Координаты точки
    coordinate0 = models.FloatField()
    coordinate1 = models.FloatField()
    # Номер точки в маршруте
    num = models.IntegerField()
    # Маршрут
    way = models.ForeignKey(Route, on_delete=models.CASCADE)
