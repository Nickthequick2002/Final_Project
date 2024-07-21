from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# Form for specifying the quantity of a product
class QuantityForm(forms.Form):
    # Integer field for quantity with label set to an empty string
    quantity = forms.IntegerField(
        label='',  # No label for the quantity field
        min_value=1,  # Minimum value for the quantity is 1
        max_value=9,  # Maximum value for the quantity is 9
        widget=forms.NumberInput(
            attrs={'class': 'form-control mt-1', 'placeholder': 'quantity'}  # CSS classes and placeholder for the input field
        )
    )
