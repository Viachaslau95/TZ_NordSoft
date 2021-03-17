from django import forms
from django.contrib.auth import authenticate
from captcha.fields import CaptchaField
from account.models import Account


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.IntegerField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Адрес', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    city = forms.CharField(label='Город', widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)

    class Meta:
        model = Account
        fields = ['email', 'first_name', 'last_name',
                  'phone', 'address', 'city']


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='Решите простой пример')

    class Meta:
        model = Account
        fields = ('email', 'password', 'captcha')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Неправильный логин или пароль')
