from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from route.forms import *
from route.models import *

# @login_required
# def add_route(request):
#     """ Добавить новый маршрут """
#
#     if request.method == 'POST':
#         form = RouteForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('/route/1')
#     else:
#         form = RouteForm()
#
#     return render(request, 'route/add.html', {'form': form})


@login_required
def add(request):
    """ Добавить новый маршрут """

    if request.method == 'POST':
        form = RouteForm(request.POST)
        print(request.POST)
        if form.is_valid():
            Route(name=form.cleaned_data['name'], owner_id=request.user.id, start_date=form.cleaned_data['start_date'],
                  end_date=form.cleaned_data['end_date']).save()
            return HttpResponseRedirect('/route/1')
    else:
        form = RouteForm()

    return render(request, 'route/add.html', {'form': form})


@login_required
def detail(request, route_id):
    route = Route.objects.get(pk=route_id)
    waypoints = route.waypoint_set.all()
    return render(request, "route/detail.html", {"route": route, "waypoints": waypoints})
