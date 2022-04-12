from django.db import models
from core.models import TimeStampModel
from car import constants


class Car(TimeStampModel):
    seller_name = models.CharField(max_length=255)
    seller_mobile = models.CharField(max_length=255)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.DateTimeField()
    condition = models.CharField(
        max_length=255,
        choices=constants.CarConditionType.choices,
        default=constants.CarConditionType.good,
    )
    price = models.PositiveIntegerField()
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.seller_name}"
