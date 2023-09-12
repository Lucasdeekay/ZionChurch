from django.urls import path
from .views import HomeView, AboutView, ContactView, GalleryView, RoadmapView, ProjectView, EventView, MenOfZionView, DaughterOfZionView

app_name = "MySite"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about-us", AboutView.as_view(), name="about"),
    path("contact-us", ContactView.as_view(), name="contact"),
    path("men-of-zion", MenOfZionView.as_view(), name="moz"),
    path("daughter-of-zion", DaughterOfZionView.as_view(), name="doz"),
    path("events", EventView.as_view(), name="events"),
    path("project", ProjectView.as_view(), name="project"),
    path("gallery", GalleryView.as_view(), name="gallery"),
    path("road-map", RoadmapView.as_view(), name="roadmap"),
]