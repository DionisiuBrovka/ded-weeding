from django.urls import path
from .views import pg_index

urlpatterns = [
    path('<int:pk>', pg_index),
]
