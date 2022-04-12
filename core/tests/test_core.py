import pytest
from django.test import RequestFactory
from core.views import DashboardListView, BuyCarView
from .factories import CarFactory, UserFactory
from datetime import datetime, timedelta
from django.contrib.auth import views as auth_views
from core.forms import SellerDetailsForm

factory = RequestFactory()
year_2014 = datetime.now() - timedelta(days=3000)
year_2016 = datetime.now() - timedelta(days=2000)


@pytest.mark.django_db
def test_car_listing():
    CarFactory(make="Mercedes‑Benz", model="A‑Class", year=year_2014, price=6000)
    CarFactory(make="Audi", model="A2", year=year_2014, price=7000)
    CarFactory(make="Audi", model="A3", year=year_2016, price=8000)
    CarFactory(make="Audi", model="A4", year=year_2016, price=9000)
    CarFactory(make="Mercedes‑Benz", model="C‑Class", year=year_2014, price=5000)

    request = factory.get("/")
    response = DashboardListView.as_view()(request)
    assert response.status_code == 200
    assert response.template_name == ["dashboard.html", "car/car_list.html"]
    assert response.context_data["car_list"].count() == 5

    request = factory.get("/?make=Audi&year=2014")
    response = DashboardListView.as_view()(request)
    response.context_data["filter"].qs.count() == 1

    request = factory.get("/?make=Audi")
    response = DashboardListView.as_view()(request)
    response.context_data["filter"].qs.count() == 3

    request = factory.get("/?year=2016")
    response = DashboardListView.as_view()(request)
    response.context_data["filter"].qs.count() == 2


@pytest.mark.django_db(transaction=True)
def test_login():
    UserFactory(username="mike@example.org", password="mikeymike123")
    request_data = {"username": "mike@example.org", "password": "mikeymike123"}
    request = factory.post("login/", data=request_data)
    request._dont_enforce_csrf_checks = True
    response = auth_views.LoginView.as_view()(request)
    assert response.status_code == 200

    UserFactory()
    request = factory.post("login/", data={})
    request._dont_enforce_csrf_checks = True
    response = auth_views.LoginView.as_view()(request)
    assert response.context_data["form"].errors == {
        "username": ["This field is required."],
        "password": ["This field is required."],
    }

    UserFactory(password="mikeymike123")
    request = factory.post(
        "login/", data={"username": "test123", "password": "mikeymike123"}
    )
    request._dont_enforce_csrf_checks = True
    response = auth_views.LoginView.as_view()(request)
    assert response.context_data["form"].errors == {
        "__all__": [
            "Please enter a correct username and password. Note that both fields may be case-sensitive."
        ]
    }


@pytest.mark.django_db(transaction=True)
def test_buy_car():
    car = CarFactory(make="Mercedes‑Benz", model="A‑Class", year=year_2016, price=6000)
    request = factory.get(f"buy/{car.id}")
    response = BuyCarView.as_view()(request, car.id)
    data = {"name": "Billy", "mobile": "9087654321"}
    form = SellerDetailsForm(data=data)
    assert form.is_valid()
    data.update({"car_id": car.id})
    request = factory.post("/register_car/", data=data)
    response = BuyCarView.as_view()(request)
    assert response.status_code == 200
    car.refresh_from_db()
    assert car.is_sold
