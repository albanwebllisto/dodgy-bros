from car import constants
import pytest
from django.test import RequestFactory
from car.views import CarCreateView
from car import forms
import datetime

factory = RequestFactory()


@pytest.mark.django_db
def test_car_registration():
    # Form is valid
    data = {
        "seller_name": "Billy",
        "seller_mobile": "9087654321",
        "make": "Mercedes‑Benz",
        "model": "A‑Class",
        "year": datetime.datetime.now(),
        "condition": constants.CarConditionType.good,
        "price": 8000,
        "is_sold": False,
    }

    form = forms.CarForm(data=data)
    assert form.is_valid()

    request = factory.post("/register_car/", data=data)
    response = CarCreateView.as_view()(request)
    assert response.status_code == 200

    # when form is not valid
    data.update({"price": 800})
    form = forms.CarForm(data=data)

    assert not form.is_valid()
    assert form._errors == {"price": ["Price must be between 1000 to 100000!"]}
