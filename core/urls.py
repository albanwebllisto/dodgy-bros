from django.urls import path
from .views import DashboardListView, BuyCarView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path("", DashboardListView.as_view(), name="dashboard"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("buy/<int:id>", BuyCarView.as_view(), name="buy"),
    path(
        "thank-you/",
        TemplateView.as_view(template_name="thank_you.html"),
        name="thank-you",
    ),
]
