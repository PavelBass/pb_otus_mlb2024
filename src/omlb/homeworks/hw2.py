"""Домашнее задание к уроку 4 "Управляющие конструкции"."""
import string
from collections import defaultdict
from typing import Literal


def task1():
    """
    Задание 1 - Пользователь вводит целое число,
    программа складывает все цифры числа, с
    полученным числом - то же самое и так до тех пор,
    пока не получится однозначное число.

    Пример:
        545 -> 5
        12345 -> 6
    """
    number = input('Введите целое число > ')
    result = 0
    while len(number) > 1:
        result = sum(map(int, number))
        number = str(result)
    print(result)


def task2():
    """
    Задание 2 - Кинотеатр, дан список списков, каждый
    вложенный список состоит из 1 и 0, Количество
    вложенных списков - количество рядов. Пользователь
    вводит сколько билетов ему требуется. Программа
    должна найти ряд, где можно приобрести нужно количество
    билетов (места должны быть рядом). Если таких рядов несколько,
    то ближайший к экрану (ближайшим считается нулевой ряд). Еcли
    таких мест нет, то вывести False

    Пример:
        [[0,1,1,0], [1, 0, 0, 0], [0,1,0,0]], 2 -> 1
        [[0,1,1,0], [1, 0, 1, 0], [1,1,0,1]], 2 -> False
    """
    number = int(input('Введите количество билетов > '))
    seats = _get_cinema_seats()
    search_for = '0' * number
    for index, row in enumerate(seats):
        casted_row = ''.join(map(str, row))
        if search_for in casted_row[index:]:
            print(index)
            break
    else:
        print(False)


def _get_cinema_seats() -> list[list[Literal[0, 1]]]:
    """Это фейковая функция. Нужна для тестов."""
    return [
        [0, 1, 1, 0],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
    ]


def task3():
    """
    Задание 3 - Написать упрощенную версию алгоритма RLE.
    Алгоритм RLE объединяет подряд идущие символы в коэффициент
    и символ.

    Пример:
        aaabbbbccccc -> 3a4b5c
        asssdddsssddd -> 1a3s3d3s3d
        abcba -> 1a1b1c1b1a
    """
    text = input('Введите текст > ')
    result = ''
    count = 0
    previous_symbol = text[0] if text else ''
    for symbol in text:
        if symbol == previous_symbol:
            count += 1
            continue
        result += f'{count}{previous_symbol}'
        previous_symbol = symbol
        count = 1
    result += f'{count or ""}{previous_symbol}'
    print(result)


def task4():
    """
    Задание 4 - Шифр Цезаря, пользователь вводит строку и
    ключ шифра, программа должна вывести зашифрованную строку
    (со сдвигом по ключу). Сдвиг циклический. Используем
    только латинский алфавит, пробелы не шифруются.

    Пример:
        Dog, 2 -> Fqi
        Zak zak, 3 -> Cdn cdn
        Python is the BEST, 5 -> Udymts nx ymj GJXY
    """
    text = input('Введите строку > ')
    key = int(input('Введите ключ > '))
    result = ''
    for symbol in text:
        if symbol not in string.ascii_letters:
            result += symbol
            continue
        symbol_position = string.ascii_lowercase.find(symbol.lower())
        new_position = (symbol_position + key) % len(string.ascii_lowercase)
        converted_symbol = string.ascii_lowercase[new_position]
        result += converted_symbol if symbol.islower() else converted_symbol.upper()
    print(result)


def task5():
    """
    Задание 5 - Табель успеваемости, пользователь в бесконечном цикле
    (пока не будет введена пустая строка) вводит строки вида:
    'название предмета' 'фамилия ученика' 'оценка'.
    После окончания ввода программа выводит в консоль Название предмета,
    далее список учеников и все их оценки в виде таблицы

    Пример:
        Математика Иванов 5
        Математика Иванов 4
        Литература Иванов 3
        Математика Петров 5
        Литература Сидоров 3
        Литература Петров 5
        Литература Иванов 4
        Математика Сидоров 3
        Математика Петров 5

        Математика
        Иванов 5 4
        Петров 5 5
        Сидоров 3

        Литература
        Иванов 3 4
        Сидоров 3
        Петров 5
    """
    grade = defaultdict(lambda: defaultdict(list))
    while True:
        data = input('"название предмета" "фамилия ученика" "оценка" > ')
        if not data:
            break
        subject, student, score = data.split()
        grade[subject][student].append(score)

    for subject, students_scores in grade.items():
        print()
        print(subject)
        for student, scores in students_scores.items():
            print(f'{student} {" ".join(scores)}')

