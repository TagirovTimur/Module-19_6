from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .forms import UserRegister
from .models import Game, Buyer, News


def platform_index(request):
    return render(request, 'task1/platform.html',
                  {'header': 'Главная страница'})


def catalog(request):
    return render(request, 'task1/games.html',
                  {'header': 'Игры',
                   'games': Game.objects.all()})


def cart(request):
    return render(request, 'task1/cart.html', {'header': 'Корзина'})


def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            error = ''
            if password != repeat_password:
                error = 'Пароли не совпадают'
                form.fields['password'].widget.attrs.update(
                    {'autofocus': '', 'class': 'col_input'})
                form.fields['repeat_password'].widget.attrs.update(
                    {'class': 'col_input'})
            elif Buyer.objects.filter(name=username).exists():
                error = 'Пользователь уже существует'
                form.fields['username'].widget.attrs.update(
                    {'autofocus': '', 'class': 'col_input'})

            if error:
                return render(request, 'task1/registration_page.html',
                              {'error': error, 'form': form})
            else:
                Buyer.objects.create(name=username, balance=0, age=age)
                return HttpResponse(f'Приветствуем, {username}!')
    else:
        return render(request, 'task1/registration_page.html',
                      {'form': UserRegister()})


def news(request):
    return render(request, 'task1/news.html',
                  {'header': 'Новости',
                   'news': Paginator(News.objects.all().order_by('-date'), 3) \
                            .get_page(request.GET.get('page', 1))})
