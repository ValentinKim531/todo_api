from django.urls import path
from .views import ScrapeView, CompanyListView

urlpatterns = [
    path("run/", ScrapeView.as_view()),
    path("companies/", CompanyListView.as_view()),
]
