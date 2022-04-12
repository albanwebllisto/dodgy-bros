from django.forms import ModelForm
from .models import Car
from django.core.exceptions import ValidationError


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

    def clean(self):
        data = self.cleaned_data
        if data["price"] < 1000 or data["price"] > 100000:
            raise ValidationError({"price": "Price must be between 1000 to 100000!"})
