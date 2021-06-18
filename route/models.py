from django.db import models
from django.contrib.auth.models import User


class Route(models.Model):
    """ Маршрут """

    # Название
    name = models.CharField(max_length=60, unique=True)
    # Владелец
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # Дата начала поездки
    start_date = models.DateTimeField(null=True)
    # Дата окончания поездки
    end_date = models.DateTimeField(null=True)
    # Описание
    description = models.TextField(null=True)


class Waypoint(models.Model):
    """ Точка маршрута """

    # Название
    name = models.CharField(max_length=60)
    # Дата начала поездки
    start_date = models.DateField(null=True)
    # Дата окончания поездки
    end_date = models.DateField(null=True)
    # Номер точки в маршруте
    num = models.IntegerField()
    # Поездка
    way = models.ForeignKey(Route, on_delete=models.CASCADE)


class Event(models.Model):
    """ Мероприятие """

    # Название
    name = models.CharField(max_length=60)
    # Дата начала
    start_date = models.DateTimeField()
    # Дата окончания
    end_date = models.DateTimeField()
    # Точка маршрута
    waypoint = models.ForeignKey(Waypoint, on_delete=models.CASCADE)
    # Описание
    description = models.TextField(null=True)


class Member(models.Model):
    """ Участник поездки """

    # Участник
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Поездка
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    # TRUE, если участник принял приглашение
    is_joined = models.BooleanField()
