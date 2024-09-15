"""Домашнее задание к уроку 3 "Базовые типы данных"."""


def task1():
    """
    Задание 1 - Пользователь вводит пятизначное число. Программа
    должна зеркально отразить центральные три цифры.
    Первая и последняя остаются на местах.

    Пример:
        23456 -> 25436
        30789 -> 38709
    """
    number = input('Введите пятизначное число > ')
    print(f'{number[0]}{number[3:0:-1]}{number[4]}')


def task2():
    """
    Задание 2 - Отпуск, пользователь вводит сколько дней
    осталось доближайшего отпуска. Программа должна вывести
    количество выходных дней до отпуска, если учесть, что
    выходные это суббота и воскресенье, сегодня понедельник
    и праздники мы не учитываем.

    Пример:
        4 -> 0
        6 -> 1
        14 -> 4
    """
    days = int(input('Сколько дней осталось до отпуска? '))

    full_weeks = days // 7
    partly_week_days = days % 7
    last_holydays = partly_week_days % 5 if partly_week_days > 4 else 0
    holydays = full_weeks * 2 + last_holydays
    print(f'До отпуска осталось {holydays} выходных')


def task3():
    """
    Задание 3 - Пользователь вводит длину и ширину плитки
    шоколада, а также размер куска, который хочет отломить,
    программа должна вычислить - можно ли совершить
    подобный разлом или нет, если учесть, что ломать можно
    только по прямой

    Пример:
        3, 4, 6 -> True
        5, 7, 8 -> False
        4, 5, 12 -> True
    """
    data = input('Введитие длину, ширину плитки шоколада и размер куска через запятую > ')
    length, witdth, size = (int(i.strip()) for i in data.split(','))
    is_size_multiple_length = size % length == 0
    is_possible = is_size_multiple_length and size < length * witdth
    print(is_possible)


def task4():
    """
    Задание 4 - Пользователь вводит целое положительное число,
    программа должна вернуть строку в виде римского числа

    Пример:
        3 -> III
        15 -> XV
        234 -> CCXXXIV
    """
    number = input('Введите целое положительное число > ')
    rules = {
        '0': '',
        '1': '{symbol}',
        '2': '{symbol}{symbol}',
        '3': '{symbol}{symbol}{symbol}',
        '4': '{symbol}{next_symbol}',
        '5': '{next_symbol}',
        '6': '{next_symbol}{symbol}',
        '7': '{next_symbol}{symbol}{symbol}',
        '8': '{next_symbol}{symbol}{symbol}{symbol}',
        '9': '{symbol}{after_next_symbol}',
    }
    roman_symbols = 'IVXLCDM'
    result = ''
    for index, character in enumerate(number[::-1]):
        index *= 2
        result = rules[character].format(
            symbol=roman_symbols[index],
            next_symbol=roman_symbols[index + 1],
            after_next_symbol=roman_symbols[index + 2]
        ) + result
    print(result)


def task5():
    """
    Задание 5 - Пользователь вводит данные, проверить - являются ли
    они положительным вещественным числом. Не использовать
    встроенные функции для проверки, только методы данных и
    конструкцию IF. (Дополнительное задание, по желанию - проверка
    на отрицательные вещественные числа)

    Пример:
        5.6 -> True
        .78 -> True
        .67. -> False
        5 -> True
        -5.6 -> True
        -.78 -> True
        -.67. -> False
        -5 -> True

    """
    number = input('Введите вещественное число > ')
    number = _clean_left_valid_non_numbers(number)
    if '.' in number:
        integer, _, fractional = number.partition('.')
        has_both_parts = integer != '' and fractional != ''
        print(has_both_parts and _contain_only_numbers(integer) and _contain_only_numbers(fractional))
    else:
        print(_contain_only_numbers(number))


def _clean_left_valid_non_numbers(value: str) -> str:
    """Очистить строку от валидных символов слева

        * Убирает знак '-'
        * Убирает '0.'
        * Убирает '.'

    Args:
        value: любая строка

    Returns:
        Строка, очищенная от валидных символов
    """
    if value.startswith('-'):
        value = value[1:]
    if value.startswith('0.'):
        value = value[2:]
    if value.startswith('.'):
        value = value[1:]
    return value


def _contain_only_numbers(value: str) -> bool:
    """Содержит ли строка только цифры

    Args:
        value: любая строка

    Returns:
        Содержит ли строка только цифры
    """
    numbers = '0123456789'
    return value != '' and all(i in numbers for i in value)

