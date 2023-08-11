from django.shortcuts import render
from .models import Invate

# Create your views here.
def pg_index(request, slug):
    obj = Invate.objects.get(slug=slug)
    return render(request, "index.html", {'data' : obj})

def pg_main(request):
    objs = Invate.objects.all()
    return render(request, "main_page.html", {'data' : objs})