from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """ Форма авторизация """

    # Имя пользователя
    username = forms.CharField()
    # Пароль
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    """ Форма регистрации """

    # Пароль
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    # Повтор пароля
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self) -> str:
        """ Сравнивает пароль и повтор пароля. Если пароли не совпадают, бросает исключение. Иначе возвращает пароль """

        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return cd['password2']
