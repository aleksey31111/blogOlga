"""todos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth (Pages for Enter Person Cubinet)
    # путь('зарегистрироваться', просмотры.зарегистрироватьпользователя, имя='зарегистрироватьпользователя')
    path('signup', views.signupuser, name='signupuser'),
    # путь('выйти/', просмотры.выйтипользователь, имя='выйтипользователь')
    path('logout/', views.logoutuser, name='logoutuser'),
    # путь('войти/', просмотры.войтипользователь, имя='войтипользователь')
    path('login/', views.loginuser, name='loginuser'),

    # Todos(Задачи)
    # путь('', просмотры.дом, имя='дом'),
    path('', views.home, name='home'),
    # путь('создать/', просмотры.создатьзадачу, имя='создатьзадачу'),
    path('create/', views.createtodo, name='createtodo'),
    # путь('текущий/', просмотры.текущиезадачи, имя='текущиезадачи'),
    path('current/', views.currenttodos, name='currenttodos'),
    # путь('задача/<целое:задача_пк>', просмотры.просмотрзадачи, имя='просмотрзадачи'),
    path('todo/<int:todo_pk>', views.viewtodo, name='viewtodo'),
    # путь('задача/<целое:задача_пк>/выполнить, просмотры.выполнитьзадачу, имя='выполнитьзадачу''
    path('todo/<int:todo_pk>/comlete', views.completetodo, name='completetodo'),
    # ('задача/<целое:задача_пк>/удалить', просмотры.удалитьзадачу, имя='удалитьзадачу')
    path('todo/<int:todo_pk>/delete', views.deletetodo, name='deletetodo'),
    # путь('выполненная/', просмотры.выпоненнаязадача, имя='выполненныязадача'),
    path('completed/', views.completedtodo, name='completedtodo'),
]
