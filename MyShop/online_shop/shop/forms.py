from django import forms
from .models import Rating

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating  # Specifies the model that the form is associated with
        fields = ['value']  # Specifies the fields to include in the form
        widgets = {
            # Specifies the widget to use for the 'value' field
            # In this case, a radio button group with choices from 1 to 5
            'value': forms.RadioSelect(choices=[(i, i) for i in range(1, 6)]),
        }
