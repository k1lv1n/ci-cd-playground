"""
Файл с простой бизнес-логикой.
"""


def hello_user(username: str = "Bob"):
    """
    Функция приветствия
    :param username: имя пользователя
    :return: приветствие пользователя
    """
    return f"Hello, {username}!"


def new_function(a: int, b: int):
    """
    Новая функция
    :param a: некое число
    :param b: некое число
    :return: сумма двух чисел
    """
    return a + b
