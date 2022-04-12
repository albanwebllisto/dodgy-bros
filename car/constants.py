from django.db import models
from django.utils.translation import gettext_lazy as _


class CarConditionType(models.TextChoices):
    """
    Class for user type choices.
    """

    poor = "POOR", _("Poor")
    fair = "REVIEWER", _("Fair")
    good = "GOOD", _("Good")
    excellent = "Excellent", _("Excellent")
