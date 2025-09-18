from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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

@login_required
def settings(request):
    from accounts.models import SecurityPhrase

    template_data = {}

    if request.method == "POST":
        phrase = request.POST.get("sec")
        if phrase and request.user.is_authenticated:
            SecurityPhrase.objects.create(phrase=phrase, user=request.user)
            template_data["message"] = "Security phrase saved successfully."
        else:
            template_data["error"] = "You must be logged in and enter a phrase."

    return render(request, "home/settings.html", {"template_data": template_data})
