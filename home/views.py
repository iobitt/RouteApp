from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from route.models import *


@login_required
def index(request):
    """ Возвращает главную страницу """

    routes = Route.objects.filter(owner_id=request.user.id)
    return render(request, "home/index.html", {"routes": routes})
