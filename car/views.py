from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import CarForm

# Create your views here.


class CarCreateView(FormView):
    template_name = "car/car_create.html"
    form_class = CarForm
    # success_url = '/thank-you/'

    def form_valid(self, form):
        # This method is called when valid form data has been POST.
        obj = form.save()
        return render(self.request, "thank_you.html", {"id": obj.id})
