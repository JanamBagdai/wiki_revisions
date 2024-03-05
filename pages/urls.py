from django.urls import path

from . import views

urlpatterns = [
    # path("", views.home, name="home"),
    path("random_number", views.random_number, name="random_number"),
    path("", views.parse_events_and_generate_graphs, name="parse_events_and_generate_graphs"),
]
    