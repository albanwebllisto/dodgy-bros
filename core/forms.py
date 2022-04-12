from django import forms


class SellerDetailsForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    mobile = forms.CharField(label="Mobile", max_length=100)
