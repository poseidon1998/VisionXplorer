from django.urls import path
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('index',index),
]
