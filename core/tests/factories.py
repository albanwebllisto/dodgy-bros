import factory
from factory.django import DjangoModelFactory
from car.models import Car
from car import constants
import random
from django.contrib.auth.models import User


class CarFactory(DjangoModelFactory):
    condition = constants.CarConditionType.good
    is_sold = False

    @factory.lazy_attribute
    def seller_name(self):
        while True:
            random_number = random.randint(0, 10000)  # noqa: S311
            seller_name = f"_user_{random_number}"
            if Car.objects.filter(seller_name=seller_name).exists():
                continue
            return seller_name

    @factory.lazy_attribute
    def seller_mobile(self):
        while True:
            seller_mobile = random.randint(9000000000, 9999999999)  # noqa: S311
            if Car.objects.filter(seller_mobile=seller_mobile).exists():
                continue
            return seller_mobile

    class Meta:
        model = Car


class UserFactory(DjangoModelFactory):
    @factory.lazy_attribute
    def username(self):
        while True:  # keep trying to find a unique username
            random_number = random.randint(0, 10000)  # noqa: S311
            username = f"user_{random_number}"
            if User.objects.filter(username=username).exists():
                continue
            return username

    class Meta:
        model = User
