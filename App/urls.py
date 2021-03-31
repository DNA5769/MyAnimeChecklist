from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('changestatus/<str:pk>/<str:status>', views.change_status),
]
