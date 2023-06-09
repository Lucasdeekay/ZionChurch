from django.shortcuts import render
from django.views import View


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


class ProjectView(View):
    template_name = "mysite/project.html"

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
