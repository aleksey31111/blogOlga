from django.shortcuts import render
from .models import Skills


def index(request):
    projects = Skills.objects.all()
    return render(request, 'skills/skills_index.html', {'projects': projects})
