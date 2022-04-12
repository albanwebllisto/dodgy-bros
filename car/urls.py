from django.urls import path
from .views import CarCreateView

urlpatterns = [
    path("register_car/", CarCreateView.as_view(), name="register-car"),
]
