import hashlib
import random

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, ValidationError
from users.models import User
import re

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        # super(UserRegisterForm, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите адрес эл. почты'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Подтвердите пароль'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
    def save(self, commit=True):
        user=super(UserRegisterForm, self).save()
        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()
        return user


    def clean(self):
        """Checks name fields length"""
        new_cleaned_data = super().clean()
        for field in new_cleaned_data:
            if len(new_cleaned_data[field]) < 3:
                raise ValidationError('Слишком короткий логин, имя или фамилия.')
        return new_cleaned_data

class UserProfileForm(UserChangeForm):
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'age', 'username', 'email', 'image')

    def __init__(self, *args, **kwargs):
        # super(UserProfileForm, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'

    # def clean_image(self):
    #     data = self.cleaned_data['image']
    #     if data and data.size > 2500000:
    #         raise forms.ValidationError('Файл слишком большой')
    #     return data
#ВОЗМОЖНО ПОЭТОМУ НЕ ГРУЗИТСЯ

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        if re.search(r'\d+', data):
            raise ValidationError('Фамилия не должна включать цифры')
        elif len(data) < 3:
            raise ValidationError('Слишком короткая фамилия')
        return data


    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        if re.search(r'\d+', data):
            raise ValidationError('Имя не должно включать цифры')
        elif len(data) < 3:
            raise ValidationError('Слишком короткое имя')
        return data


