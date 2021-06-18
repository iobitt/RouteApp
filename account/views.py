from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


def user_login(request):
    """ Авторизовать пользователя """

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Авторизация прошла успешно!')
                else:
                    return HttpResponse('Аккаунт деактивирован!')
            else:
                return HttpResponse('Не верный логин!')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    """ Зарегистрировать пользователя """

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('/')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': user_form})


@login_required
def logout_view(request):
    """ Деавторизовать пользователя """

    logout(request)
    return redirect('/accounts/login/')
