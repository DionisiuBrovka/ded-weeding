from django.shortcuts import render
from .models import Invate

# Create your views here.
def pg_index(request, pk=1):
    obj = Invate.objects.get(id=pk)
    return render(request, "index.html", {'data' : obj})