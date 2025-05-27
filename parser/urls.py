from django.urls import path
from .views import ScrapeView, CompanyListView

urlpatterns = [
    path("parse/", ScrapeView.as_view()),
    path("results/", CompanyListView.as_view()),
]
