# из джанго.ярлыки импортировать визуализировать(передавать, оказывать,),перенаправить,получить_обьект_или_404
from django.shortcuts import render, redirect, get_object_or_404
# из джанго.вклад.авторизации.формы импортировать ПользовательСозданиеФорма, АутонтификацияФорма
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# из джанго.вклад.авторизация.модели импортировать Поьзователь
from django.contrib.auth.models import User
# из джанго.дб импортировать ЦелостностиОшибка
from django.db import IntegrityError
# из джанго.вклад.авторизации импортировать вход, выход, аутентификация
from django.contrib.auth import login, logout, authenticate
# из джанго.утилиты импортировать часовойпояс
from django.utils import timezone

# из .формы импортировать ЗадачаФорма
from .forms import TodoForm
# из .моделей импортировать Задача
from .models import Todo
# из джанго.вклад.авторизация.декорвторы импортировать вход_запрос
from django.contrib.auth.decorators import login_required



def home(request):
    """
определение дом(запрос):
    :param request:
    :return: вернуть визализировать(запрос, 'задача/дом.html')
    """
    return render(request, 'todo/home.html')


def signupuser(request):
    """
    определение Страница Регистрации(запрос):
    Если запрос.метод == 'ПОЛУЧАТЬ'
        :return: передавать(запрос, 'задача/зарегистрироватьпользователя.html', {'форма': ПользовательЗозданиеФормы()})
    Иначе:
        Если запрос.ПОЧТА['пароль1']==запрос.ПОЧТА['пароль2']

        попытаться:
            пользователь=Поьзователь.обьекты.создать_пользователя(запрос.ПОЧТА['пользовательимя'],
            пароль=запрос.ПОЧТА['пароль1']
            :return перенаправить('текущиезадачи')
        исключение ЦелаяОшибка:
            вернуть передавать(запрос, 'задача/зарегистрироватьпользователя.html', {'форма': ПльзовательСозданиеФормы()',
            'ошибка':'Такое имя пользователя есть'
    else:
        вернуть передавать(запрос, 'задача/зарегистрироватьпользователя.html',
            {'форма': ПользовательСозданиеФормы(), 'ошибка':'Пароли не совпадают"}
    """
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                # user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form': UserCreationForm(),
                                                                'error': 'Такое имя пользователя'
                                                                         'уже существует. Задайте дркгое.'})
        else:
            return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'Пароли не совпадает'})


def logoutuser(request):
    """
    Выход пользователя(запос):
    Если request: запрос.метод=='ПОЧТА':
        выход(запрос)
        :return: перенаправить('дом')
    """
    if request.method == 'POST':
        logout(request)
        return redirect('home')


@login_required
def currenttodos(request):
    """
    Страница текущих задач
    :return: render(request, 'todo/currenttodos.html')
    """
    todos = Todo.objects.filter(user=request.user, date_completed__isnull=True)
    return render(request, 'todo/currenttodos.html', {'todos': todos})


def loginuser(request):
    """
    Вход пользователя
    if:
        :param request: request.method == 'GET':
        :return: return render(request, 'todo/loginuser.html', {'form':AuthenticationForm()})
    else:
        пользователь=аутентифицировать(запрос, пользовательимя=запрос.ПОЧТА['пользовательимя'],
        пароль=запрос.ПОЧТА['пароль'])
        if
            :param пользователь является Нет:
            : вернуть передать(запрос, 'todo/логинпользователь.html',
                {'форма': АутентификацияФорма(), 'ошибка':'Нверные данные'})
        else:
            :param: авторизироваться(запрос, пользователь)
            :вернуть перенаправить('текущиезадачи')

    """
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        # user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login/loginuser.html', {'form': AuthenticationForm(),
                                                            'error': 'Неверные данные'})
        else:
            login(request, user)
            return redirect('currenttodos')


@login_required
def createtodo(request):
    """
    if
        :param запрос.метод == 'ПОЛУЧАТЬ'
        :return: передать(запрос, 'todo/создатьзадачи.html')
    else:
        Попытаться:
            форма =TodoForm(request.POST)
            Новый_todo = форма.сохранить(commit=False)
            Новый_todo.пользователь = запрос.пльзователь
            Новый_todo.сохранить
            вернуть перенаправить('текущиезадачи.html')
        Исключение ЗначениеОшибка:
            вернуть передать(запрос, 'todo/создатьзадачи.html', {'форма'：ЗадачаФорма(),
            'Ошибка': 'Переданны неверные данные попробуйте еще раз'})
    """
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/createtodo.html', {'form': TodoForm(),
                                                            'error': 'Переданы неверные данные.'
                                                            'Попробуйте еще наз.'})


@login_required
def viewtodo(request, todo_pk):
    """

    :param request:
    :param todo_pk: задачи = получить_обьект_или_404(Задачи, pk=задачи_pk)
    #:return: вернутьзапрос, 'todo/просмотрзадачи.html', {'задачи': задачи})
    if запрос.метод == 'ПОЛУЧИТЬ':
        форма = ЗапросФорма(экземпляр=запрос)
        вернуть передать(запрос, 'задача/просмотрзадачи.html',
            {'задача': задача, 'форма': форма}
    иначе:
        пробовать:
            форма = ЗадачаФорма(запрос.ПОЧТА, эземпляр=задача)
            форма.сохранить()
            вернуть перенаправить("текущаязадача")
        исключение ЗначениеОшибка:
            вернуть передача(запрос, ,'задача/просмотрзадачаюhtml',
            {‘задача’:задача, 'форма': форма,
            'ощибка':'Неверные данные'}
    """
    todo = get_object_or_404(Todo, pk=todo_pk)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/viewtodo.html', {'todo': todo,
                                                      'form': form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/viewtodo.html',
                          {'todo': todo, 'form': form,
                           'error': 'Неверные данные'})


@login_required
def completetodo(request, todo_pk):
    """
    из джанго.утилиты импорт времязоны
    :param request(запрос):
    :param todo_pk(задача_пк):
    задачи = получить_обьект_или_404(Задачи, пк=задача_пк, пользователь=запрос.пользователь)
    если запрос.метод == 'ПОЧТА':
        задача.время_выполнения = времязоны.сейчас()
        задача.сохранить()
    :return: перенаправить('текущиезадачи')
    """
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.date_completed = timezone.now()
        todo.save()
        return redirect('currenttodos')


@login_required
def deletetodo(request, todo_pk):
    """
    :param request:
    :param todo_pk:
    задача = получить_обьект_или_404(Задачи, пк=задачи_пк, пользователь=запрос.пользователь)
    Если запрос.метод == 'ПОЧТА':
        задача.удалить()
        :return: перенаправить('текущиезадачи')
    """
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('currenttodos')


@login_required
def completedtodo(request):
    """
    :param request:
    задача = Задачи.обьект.фильтр(пользователь=запрос.пользователь,
        дата_выполнения__являетсянуль=Ложь).сщртировка_по('-дата_выполнения')
    :return: представлять(запрос, 'задача/выполненнаязадача.html', {'задачи': задачи})
    """
    todos = Todo.objects.filter(user=request.user, date_completed__isnull=False).\
        order_by('-date_completed')
    return render(request, 'todo/completedtodo.html', {'todos': todos})




