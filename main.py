""" Модуль string для работы со строками и secrets для безопасности """

import string
import secrets

class GenerateSecret:
    """ Класс для генерации паролей """

    def __init__(self, length: int = 12) -> None:
        """ Инициализация """

        self.length = length

    def generate(self):
        """ Генерируем пароль """

        password = ""

        level = input("Введите уровень сложности пароля (easy, medium, hard): ").lower()

        match level:
            case "easy":
                available = string.ascii_lowercase + string.ascii_uppercase
            case "medium":
                available = string.ascii_lowercase + string.ascii_uppercase + string.digits
            case "hard":
                available = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
            case _:
                print("Неизвестно. Выбираем medium\n")
                available = string.ascii_lowercase + string.ascii_uppercase + string.digits

        for _ in range(self.length):
            password += secrets.choice(available)

        return f"Ваш пароль: {password}"

    def __str__(self):
        """ Удобное представление объекта при прямом обращении """

        return self.generate()

try:
    my_length = int(input("Введите длину вашего пароля (default = 12): "))

except ValueError:
    print("Ошибка в значении")
except Exception as e:
    print(f"Ошибка: {e}")
else:
    run = GenerateSecret(my_length)

    print(run)
