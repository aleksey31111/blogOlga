# из джанго.дб импортировать моделей
from django.db import models
# из джанго.вклад.авторизации импортировать Пользователь
from django.contrib.auth.models import User


class Todo(models.Model):
    """
класс Задача(моделей.Модель):
    название = моделей.СимволПоле(максимальная_длинна=100)
    памятка = моделей.ТекстПоле(пустой=Правда)
    создано =моделей.ДатаВремяПоле(автоматический_сейчас_добавить=Правда)
    дата_завершено = моделей.ДатаВремяПоле(ноль=Правда, пустой=Правда)
    важный = моделей.БулевоПоле(поумолчанию=Ложь)
    урл = моделей.УРЛПоле(Пустой=Правда)
    пользователь = моделей.ИностранныйКлюч(Пользователь, на_удаление=моделей.КАСКАД)

определение __стр__(сам):
    вернуть сам(название)
    """
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    url = models.URLField(blank=True)
    # Каждый пользователь Видит Только Свои Записи.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
