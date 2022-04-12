from django.shortcuts import render
from django.views.generic.list import ListView
from car.models import Car
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SellerDetailsForm
from django.views import View
from django.core.mail import send_mail
from django.db.models import Q
import django_filters


class CarFilter(django_filters.FilterSet):
    class Meta:
        model = Car
        fields = ["make", "year"]

    @property
    def qs(self):
        parent = super().qs
        make = self.data.get("make")
        year = self.data.get("year")
        if bool(make) and bool(year):
            return parent.filter(Q(make=make) & Q(year__year=year))
        if bool(make) and not bool(year):
            return parent.filter(make=make)
        if bool(year) and not bool(make):
            return parent.filter(year__year=year)
        return parent


class DashboardListView(ListView):
    model = Car
    paginate_by = 10
    template_name = "dashboard.html"
    filterset_class = CarFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        objects = self.model.objects.all().order_by("-created")
        filter_data = CarFilter(self.request.GET, queryset=objects)
        paginator = Paginator(filter_data.qs, self.paginate_by)
        page = self.request.GET.get("page")
        try:
            car_list = paginator.page(page)
        except PageNotAnInteger:
            car_list = paginator.page(1)
        except EmptyPage:
            car_list = paginator.page(paginator.num_pages)
        context["object_list"] = car_list
        context["filter"] = filter_data
        return context


class BuyCarView(View):
    form_class = SellerDetailsForm
    template_name = "car/buy_details.html"

    def get(self, request, id, *args, **kwargs):
        return render(
            request, self.template_name, {"form": self.form_class(), "car_id": id}
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        car_id = form.data.get("car_id")
        if form.is_valid():
            name = form.cleaned_data.get("name")
            mobile = form.cleaned_data.get("mobile")
            car_detials = Car.objects.get(id=car_id)
            commission = round(float(car_detials.price) * float(0.05))
            net_amount = round(float(car_detials.price) + float(commission))
            vehicle_details = f"Car Detail:manufacturer:{car_detials.make} model:{car_detials.model}  \
                year:{car_detials.year} condition type: {car_detials.condition}  "
            seller_details = f"Seller Information:first name:{car_detials.seller_name}  \
                and mobile_number:{car_detials.seller_mobile}  "
            selling_price = f" Selling price:{car_detials.price}  "
            buyer_details = (
                f"Buyer Information:first name:{name} and mobile_number:{mobile}  "
            )
            commision = f" Dodgy Brother commission:{commission}  "
            net_car_price = f" Net price of car:{net_amount}  "
            message = (
                vehicle_details
                + seller_details
                + buyer_details
                + selling_price
                + commision
                + net_car_price
            )
            try:
                car_detials.is_sold = True
                car_detials.save()
                send_mail(
                    "Buy Car",
                    message,
                    "dodgybrother@gmail.com",
                    ["mike@example.or"],
                    fail_silently=False,
                )
            except Exception:
                pass
            return render(request, "success.html")
        return render(request, self.template_name, {"form": form})
