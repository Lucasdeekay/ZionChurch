from django.urls import path
from .views import HomeView, AboutView, ContactView, GalleryView, RoadmapView, ProjectView

app_name = "MySite"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about-us", AboutView.as_view(), name="about"),
    path("contact-us", ContactView.as_view(), name="contact"),
    path("project", ProjectView.as_view(), name="project"),
    path("gallery", GalleryView.as_view(), name="gallery"),
    path("road-map", RoadmapView.as_view(), name="roadmap"),
]