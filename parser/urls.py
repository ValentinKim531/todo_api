from django.urls import path
from .views import ScrapeView


urlpatterns = [path("run/", ScrapeView.as_view())]
