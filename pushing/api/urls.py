from django.contrib import admin
from django.urls import path
from .views import MessageAPIView

urlpatterns = [
    path('test', MessageAPIView.as_view())
]