from django.urls import path
from .views import RegisterView, EmailTokenObtainPairView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", EmailTokenObtainPairView.as_view()),
]
