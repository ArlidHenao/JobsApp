from django.urls import path
from django.contrib import admin
from . import views
from . import serializers

urlpatterns = [
    path('', views.holamundo)
]