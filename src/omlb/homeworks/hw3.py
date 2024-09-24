import math
from collections import namedtuple
from collections.abc import Generator
from datetime import datetime


def task1():
    """
    Задание 1 - ddddНаписать функцию, которая будет
    перводит снейк_кейс в КэмелКейс и наоборот.
    Функция сама определяет - какой формат ей передали.
    Можно добавить ключевой аргумент, который будет
    принудительно возвращать один из форматов.

    Пример:
        otus_course -> OtusCourse
        PythonIsTheBest -> python_is_the_best
    """
    string = input('Введите строку > ')
    is_snake_case = '_' in string
    formatter = _snake_case_to_camel_case if is_snake_case else _camel_case_to_snake_case
    print(formatter(string))


def _camel_case_to_snake_case(string: str) -> str:
    """Переводит строку, написанную в формате CamelCase в snake_case

    Args:
        string: Строка, написанная в CamelCase

    Returns:
        Строка, написанная в snake_case
    """
    if not string:
        return ''
    result = string[0].lower()
    last_upper_position = 0
    for position, symbol in enumerate(string[1:], 1):
        if symbol.isupper():
            result += f'{string[last_upper_position + 1:position]}_{symbol.lower()}'
            last_upper_position = position
    result += string[last_upper_position + 1:]
    return result


def _snake_case_to_camel_case(string: str) -> str:
    """Переводит строку, написанную в формате snake_case в CamelCase

    Args:
        string: Строка, написанная в snake_case

    Returns:
        Строка, написанная в CamelCase
    """
    result = ''
    for symbol in string.split('_'):
        result += symbol.title()
    return result


def task2():
    """
    Задание 2 - Написать функцию проверяющую валидность введенной даты.
    Пример:
        29.02.2000 -> True
        29.02.2001 -> False
        31.04.1962 -> False
    """
    date = input('Введите дату > ')
    try:
        datetime.strptime(date, '%d.%m.%Y')
        print(True)
    except ValueError:
        print(False)


def task3():
    """
    Задание 3 - Функция проверки на простое число.
    Простые числа – это такие числа, которые делятся
    на себя и на единицу.

    Пример:
        17 -> True
        20 -> False
        23 -> True
    """
    value = int(input('Введите число > '))
    for number in range(2, int(math.sqrt(value)) + 1):
        if value % number == 0:
            print(False)
            return
    print(True)


def task4():
    """
    Задание 4 - Пользователь в бесконечном цикле вводит данные
    пользователей: имя, затем фамилию, возраст и ID. Ввод
    продолжается до тех пор, пока не будет введено пустое поле.
    Пользователи заносятся в словарь, где ключ это ID пользователя,
    а остальные данные записываются в виде кортежа. Так же
    программа должна проверять, что имя и фамилия состоят только
    из символов и начинаются с большой буквы, если не с большой,
    то заменяет на большую, возраст должен быть числом
    от 18 до 60, ID - целое число, дополненное до 8 знаков
    незначащими нолями, ID должен быть уникальным.
    Дополнительно написать функцию, которая будет выводить
    полученный словарь в виде таблицы
    """
    users = {}
    for user_data in get_users():
        try:
            normalized_user_data = _normalize_user_data(user_data)
            _validate_user_data(user_data, normalized_user_data)
        except ValueError as exception:
            print(f'Ошибка ввода: {exception}')
            print('Попробуйте ещё раз. Для окончания ввода введите пустую строку')
            continue
        users[normalized_user_data.id] = normalized_user_data
    _print_as_table(users)


UserInputData = namedtuple('UserInputData', 'name surname age id')


def _sensitive_input(prompt: str) -> str:
    """Ввод чувствительный к вводу пустой строки.

    Args:
        prompt: Строка - приглашение для ввода

    Returns:
        Введенное значение

    Raises:
        StopIteration: Если введена пустая строка
    """
    value = input(prompt)
    if not value:
        raise ValueError('Пустая строка')
    return value


def get_users() -> Generator[UserInputData, None, None]:
    """Данные пользователей"""
    while True:
        try:
            yield UserInputData(
                name=_sensitive_input('Введите имя > '),
                surname=_sensitive_input('Введите фамилию > '),
                age=_sensitive_input('Введите возраст > '),
                id=_sensitive_input('Введите ID > '),
            )
        except ValueError:
            break


def _normalize_user_data(user: UserInputData) -> UserInputData:
    """Нормализация данных пользователя

    Args:
        user: Данные пользователя

    Returns:
        Нормализованные данные пользователя

    Raises:
        ValueError: Если возраст или ID не являются целыми числами
    """
    return UserInputData(
        name=user.name.title(),
        surname=user.surname.title(),
        age=int(user.age),
        id=int(user.id),
    )


def _validate_user_data(user_data: UserInputData, normalized_user_data: UserInputData) -> None:
    """Валидация данных пользователя

    Args:
        user_data: Данные пользователя
        normalized_user_data: Нормализованные данные пользователя

    Raises:
        ValueError: Если возрасть, не находится в диапазоне от 18 до 60
        ValueError: Если ID не является целым восьмизначным числом
    """
    if not (18 <= normalized_user_data.age <= 60):
        raise ValueError(f'Возраст должен быть числом от 18 до 60, получено {normalized_user_data}')
    if not (normalized_user_data.id > 0 and len(user_data.id) == 8):
        raise ValueError(f'ID должен быть целым восьмизначным числом, получено {normalized_user_data}')


def _print_as_table(users: dict[int, UserInputData]) -> None:
    """Вывод пользователей в виде таблицы

    Пример результата:

    N  | name     | surname   | age  | id        |
    ---| ---------| ----------| -----| ----------|
     1 | Павел    | Басс      | 41   | 34531570  |
     2 | Кирилл   | Панфилов  | 36   | 12345678  |
     3 | Евгений  | Романов   | 30   | 12345679  |

    Args:
        users: Словарь с пользователями
    """
    _print_table_head(users)
    _print_table_body(users)


def _get_max_length(users: dict[int, UserInputData]) -> dict[str, int]:
    """Получение максимальной длины полей

    Словарь с максимальной длиной полей, включая длину для нумерации.
    Эти данные необходимы для выравнивания таблицы

    Args:
        users: Словарь с пользователями

    Returns:
        Словарь с максимальной длиной полей
    """
    max_lengths = {field: len(field) for field in UserInputData._fields}
    max_lengths['N'] = len(str(len(users)))
    for user in users.values():
        for field in UserInputData._fields:
            value = getattr(user, field)
            max_lengths[field] = max(max_lengths[field], len(str(value)))
    return max_lengths


def _print_table_head(users: dict[int, UserInputData]) -> None:
    """Печатает названия колонок таблицы, включая нумерацию

    Args:
        users: Словарь с пользователями
    """
    columns = ['N']
    columns.extend(UserInputData._fields)
    max_lengths = _get_max_length(users)
    line = ''
    underline = ''
    for field in columns:
        line += f'{field:<{max_lengths[field] + 2}}| '
        underline += f'{"-" * (max_lengths[field] + 2)}| '
    print(line)
    print(underline)


def _print_table_body(users: dict[int, UserInputData]) -> None:
    """Печать тела таблицы построчно, включая колонку номера строк

    Args:
        users: Словарь с пользователями
    """
    max_lengths = _get_max_length(users)
    for number, user in enumerate(users.values(), 1):
        print(f'{number:^{max_lengths['N'] + 2}}| ', end='')
        for field in UserInputData._fields:
            value = getattr(user, field)
            print(f'{value:<{max_lengths[field] + 2}}| ', end='')
        print()

