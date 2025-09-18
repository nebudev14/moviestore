from django.shortcuts import render

from movies.models import Review


def index(request):
    template_data = {}
    template_data["title"] = "Movies Store"
    template_data["reviews"] = Review.objects.all()
    return render(request, "home/index.html", {"template_data": template_data})


def about(request):
    template_data = {}
    template_data["title"] = "About"
    return render(request, "home/about.html", {"template_data": template_data})

