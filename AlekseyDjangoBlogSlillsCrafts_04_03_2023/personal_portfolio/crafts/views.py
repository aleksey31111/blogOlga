from django.shortcuts import render
from .models import Crafts


def index(request):
    projects = Crafts.objects.all()
    return render(request, 'crafts/crafts_index.html', {'projects': projects})
