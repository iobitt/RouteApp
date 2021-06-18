"""RouteApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from account import views as account
from home import views as home
from route import views as route


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/register/', account.register, name='register'),
    path('accounts/logout/', account.logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home.index, name="index"),
    path('invitations/', route.invitations, name="invitations"),
    path('route/add', route.add, name="add"),
    path('route/<int:route_id>', route.detail, name='detail'),
    path('route/<int:route_id>/add-waypoint', route.add_waypoint, name='add_waypoint'),
    path('route/<int:route_id>/event/add', route.add_event, name='add_event'),
    path('route/<int:route_id>/member/add', route.add_member, name='add_member'),
    path('route/<int:route_id>/print', route.print_page, name='print_page'),
]
