from django.urls import path
from .views import pg_index, pg_main

urlpatterns = [
    path('<slug:slug>', pg_index),
    path('', pg_main),
]
