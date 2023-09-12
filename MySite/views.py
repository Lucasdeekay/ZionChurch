from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from MySite.models import Student


class HomeView(View):
    template_name = "mysite/home.html"

    def get(self, request):
        return render(request, self.template_name)


class AboutView(View):
    template_name = "mysite/about.html"

    def get(self, request):
        return render(request, self.template_name)


class ContactView(View):
    template_name = "mysite/contact.html"

    def get(self, request):
        return render(request, self.template_name)


class EventView(View):
    template_name = "mysite/events.html"

    def get(self, request):
        return render(request, self.template_name)


class ProjectView(View):
    template_name = "mysite/project.html"

    def get(self, request):
        return render(request, self.template_name)


class MenOfZionView(View):
    template_name = "mysite/moz.html"

    def get(self, request):
        return render(request, self.template_name)


class DaughterOfZionView(View):
    template_name = "mysite/doz.html"

    def get(self, request):
        return render(request, self.template_name)


class GalleryView(View):
    template_name = "mysite/gallery.html"

    def get(self, request):
        return render(request, self.template_name)


class RoadmapView(View):
    template_name = "mysite/roadmap.html"

    def get(self, request):
        return render(request, self.template_name)


def register(request):
    if request.METHOD == "POST":
        first_name = request.POST.get("first_name").strip().upper()
        last_name = request.POST.get("last_name").strip().upper()
        email = request.POST.get("email").strip().upper()

        if Student.objects.filter(email=email).exists():
            messages.success(request, "Registration successful")
        else:
            Student.objects.create(first_name=first_name, last_name=last_name, email=email)
            messages.success(request, "Registration successful")

        return HttpResponseRedirect(reverse("MySite:home"))


def error_404(request, exception):
    return render(request, 'mysite/400.html')


def error_500(request):
    return render(request, 'mysite/400.html')