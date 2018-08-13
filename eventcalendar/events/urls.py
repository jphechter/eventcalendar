from django.http import HttpResponse
from django.urls import path

from . import views
from .models import Event, Venue

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:event_id>/', views.details, name='details'),
]