from django import forms
from django.forms import ModelForm

from mainapp.models import ProductCategory, Product
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User

class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email','first_name', "last_name", "password1", 'password2', 'image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'image':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control py-4'

class UserAdminProfileForm(UserProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False

class CategoryProductsForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name == 'image':
                field.widget.attrs['class'] = 'form-control py-4'

class ProductsForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'print', 'quantity', 'category', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'image':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control py-4'
