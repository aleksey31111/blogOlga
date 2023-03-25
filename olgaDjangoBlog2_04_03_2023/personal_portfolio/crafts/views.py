from django.shortcuts import render, get_object_or_404
from .models import Crafts


def index(request):
    projects = Crafts.objects.all()
    return render(request, 'blog/blogs.html', {'projects': projects})


def crafts(request):
    blog = Crafts.objects.order_by("-date")
    return render(request, 'blog/blogs.html', {'blogs': blog})


def detail(request, crafts_id):
    blog = get_object_or_404(Crafts, pk=crafts_id)
    return render(request, 'blog/details.html', {'blog': blog})
