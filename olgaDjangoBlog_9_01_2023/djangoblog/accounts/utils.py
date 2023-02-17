import typing
from datetime import timedelta

from django.core.cache import cache

from djangoblog.utils import send_email

_code_ttl = timedelta(minutes=5)


def send_verify_email(to_mail: str, code: str, subject: str = "邮件验证码"):
    """Отправить код подтверждения сброса пароля
    Args:
        to_mail: принять электронную почту
        subject: Тема письма
        code: проверочный код
    """
    html_content = f"Вы сбрасываете свой пароль, код подтверждения:{code}, " \
                   f"Действителен в течение 5 минут, храните его в безопасности."
    send_email([to_mail], subject, html_content)


def verify(email: str, code: str) -> typing.Optional[str]:
    """Убедитесь, что код действителен
    Args:
        email: запрос по электронной почте
        code: проверочный код
    Return:
        Возвращает строку ошибки, если есть ошибка
    Node:
        Обработка ошибок здесь неразумна, следует использовать повышение
        Никакой тестовый вызывающий объект также не должен обрабатывать ошибку
    """
    cache_code = get_code(email)
    if cache_code != code:
        return "Ошибка кода подтверждения"


def set_code(email: str, code: str):
    """установить code"""
    cache.set(email, code, _code_ttl.seconds)


def get_code(email: str) -> typing.Optional[str]:
    """Получить code"""
    return cache.get(email)