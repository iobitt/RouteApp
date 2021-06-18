from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from route.forms import *
from route.models import *
import datetime


@login_required
def add(request):
    """ Добавить новую поездку """

    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            r = Route(name=form.cleaned_data['name'], owner_id=request.user.id,
                      start_date=form.cleaned_data['start_date'], end_date=form.cleaned_data['end_date'],
                      description=form.cleaned_data['description'])
            r.save()
            return HttpResponseRedirect(f'/route/{r.id}')
    else:
        form = RouteForm()

    return render(request, 'route/add.html', {'form': form})


@login_required
def detail(request, route_id: int):
    """ Вернуть страницу поездки """

    # Поездка
    route = Route.objects.get(pk=route_id)
    # Пункты маршрута
    waypoints = route.waypoint_set.all()
    # Участники поездки
    members = route.member_set.all()

    # Расчёт времени

    # Список мероприятий
    events = list()
    # Список длительностей мероприятий
    timing = list()
    # Общее время мероприятий в секундах
    total_duration = 0
    # Проходим по всем пунктам маршрута
    for waypoint in waypoints:
        # Проходим по всем мероприятиям в этом пункте
        for event in waypoint.event_set.all():
            events.append(event)

            e = dict()
            e['name'] = event.name
            duration = event.end_date.timestamp() - event.start_date.timestamp()
            e['duration'] = datetime.datetime.utcfromtimestamp(duration)
            timing.append(e)

            total_duration += duration
    # Преобрзауем число секунд в datetime.datetime
    total_duration = datetime.datetime.utcfromtimestamp(total_duration)

    return render(request, "route/detail.html", {"route": route, "waypoints": waypoints, 'events': events,
                                                 "timing": timing, "total_time": total_duration, "members": members})


@login_required
def add_waypoint(request, route_id: int):
    """ Добавить новый пункт маршрута """

    # Поездка
    route = Route.objects.get(pk=route_id)
    # Список кортежей: (ID пункта, название пункта)
    waypoints = list()
    for i in route.waypoint_set.all():
        waypoints.append((i.id, i.name))

    if request.method == 'POST':
        form = WaypointForm(request.POST, neighbours=waypoints)
        if form.is_valid():
            Waypoint(name=form.cleaned_data['name'], num=1, way=route).save()
            return HttpResponseRedirect(f'/route/{route_id}')
    else:
        form = WaypointForm(neighbours=waypoints)

    return render(request, 'route/add-waypoint.html', {'form': form, 'route_id': route_id, "waypoints": waypoints})


@login_required
def add_event(request, route_id: int):
    """ Добавить мероприятие """

    route = Route.objects.get(pk=route_id)
    waypoints = list()
    for i in route.waypoint_set.all():
        waypoints.append((i.id, i.name))

    if request.method == 'POST':
        form = EventForm(request.POST, waypoints=waypoints)
        if form.is_valid():
            waypoint = Waypoint.objects.get(pk=form.cleaned_data['waypoint'])
            Event(name=form.cleaned_data['name'], waypoint=waypoint, start_date=form.cleaned_data['start_date'],
                  end_date=form.cleaned_data['end_date'], description=form.cleaned_data['description']).save()
            return HttpResponseRedirect(f'/route/{route_id}')
    else:
        form = EventForm(waypoints=waypoints)

    return render(request, 'route/add-event.html', {'route_id': route_id, "waypoints": waypoints, 'form': form})


@login_required
def add_member(request, route_id):
    """ Добавить участника в поездку """

    route = Route.objects.get(pk=route_id)
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(username=form.cleaned_data['login'])

                if user.id == request.user.id:
                    form.add_error("login", 'Нельзя добавить самого себя')
                else:
                    Member(user=user, route=route, is_joined=False).save()
                    return HttpResponseRedirect(f'/route/{route_id}')
            except User.DoesNotExist:
                form.add_error("login", 'Пользователь не существует')
    else:
        form = MemberForm()

    return render(request, 'route/add-member.html', {'route_id': route_id, 'form': form})


@login_required
def invitations(request):
    """ Возвращает страницу со списком приглашений пользователя """

    return render(request, 'route/invitations.html', {"invitations": request.user.member_set.all()})


@login_required
def print_page(request, route_id):
    """ Возвращает страницу для печати """

    route = Route.objects.get(pk=route_id)
    waypoints = route.waypoint_set.all()
    return render(request, "route/../vkr/print.html", {"route": route, "waypoints": waypoints})
