from django import forms
from django.forms import ModelForm
from shop.models import Product, Category
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# Form for adding a new product
class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price']

    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        # Apply 'form-control' class to all visible fields for Bootstrap styling
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

# Form for adding a new category
class AddCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'sub_category', 'is_sub']

    def __init__(self, *args, **kwargs):
        super(AddCategoryForm, self).__init__(*args, **kwargs)
        # Apply specific classes to individual fields for Bootstrap styling
        self.fields['is_sub'].widget.attrs['class'] = 'form-check-input'
        self.fields['sub_category'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['class'] = 'form-control'

# Form for editing an existing product
class EditProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price']

    def __init__(self, *args, **kwargs):
        super(EditProductForm, self).__init__(*args, **kwargs)
        # Apply 'form-control' class to all visible fields for Bootstrap styling
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

# Form for user login
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        # Initialize crispy forms helper
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        # Add a submit button with the label 'Login'
        self.helper.add_input(Submit('login', 'Login'))
