import pytest

from omlb.homeworks.hw2 import (
    task1,
    task2,
    task3,
    task4,
    task5,
)


@pytest.mark.parametrize(
    'value, expected',(
        ('545', 5),
        ('12345', 6),
    )
)
def test_task1__print_expected(value, expected, mocker):
    # arrange
    mocked_input = mocker.patch('omlb.homeworks.hw2.input', return_value=value)
    mocked_print = mocker.patch('omlb.homeworks.hw2.print')

    # act
    task1()

    # assert
    mocked_print.assert_called_once_with(expected)


@pytest.mark.parametrize(
    'seats, tickets, expected',(
        ([[0, 1, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0]], 2, 1),
        ([[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1]], 2, False),
    )
)
def test_task2__print_expected(seats, tickets, expected, mocker):
    # arrange
    mocker_get_cinema_seats = mocker.patch('omlb.homeworks.hw2._get_cinema_seats', return_value=seats)
    mocked_input = mocker.patch('omlb.homeworks.hw2.input', return_value=tickets)
    mocked_print = mocker.patch('omlb.homeworks.hw2.print')

    # act
    task2()

    # assert
    mocked_print.assert_called_once_with(expected)


@pytest.mark.parametrize(
    'text, output', (
        ('aaabbbbccccc', '3a4b5c'),
        ('asssdddsssddd', '1a3s3d3s3d'),
        ('abcba', '1a1b1c1b1a'),
        ('', ''),
        ('a', '1a'),
    )
)
def test_task3__print_expected(text, output, mocker):
    # arrange
    mocked_input = mocker.patch('omlb.homeworks.hw2.input', return_value=text)
    mocked_print = mocker.patch('omlb.homeworks.hw2.print')

    # act
    task3()

    # assert
    mocked_print.assert_called_once_with(output)


@pytest.mark.parametrize(
    'text, key, output', (
        ('Dog', 2, 'Fqi'),
        ('Zak zak', 3, 'Cdn cdn'),
        ('Python is the BEST', 5, 'Udymts nx ymj GJXY'),
        ('', 5, ''),
    )
)
def test_task4__print_expected(text, key, output, mocker):
    # arrange
    mocked_input = mocker.patch('omlb.homeworks.hw2.input', side_effect=[text, key])
    mocked_print = mocker.patch('omlb.homeworks.hw2.print')

    # act
    task4()

    # assert
    mocked_print.assert_called_once_with(output)


@pytest.mark.parametrize(
    'texts, output_lines', ((
        (
            'Математика Иванов 5',
            'Математика Иванов 4',
            'Литература Иванов 3',
            'Математика Петров 5',
            'Литература Сидоров 3',
            'Литература Петров 5',
            'Литература Иванов 4',
            'Математика Сидоров 3',
            'Математика Петров 5',
            '',
        ),
        (
            None,
            'Математика',
            'Иванов 5 4',
            'Петров 5 5',
            'Сидоров 3',
            None,
            'Литература',
            'Иванов 3 4',
            'Сидоров 3',
            'Петров 5',
        )
    ),)
)
def test_task5__print_expected(texts, output_lines, mocker):
    # arrange
    mocked_input = mocker.patch('omlb.homeworks.hw2.input', side_effect=texts)
    mocked_print = mocker.patch('omlb.homeworks.hw2.print')

    # act
    task5()

    # assert
    assert mocked_print.mock_calls == [mocker.call(line) if line is not None else mocker.call() for line in output_lines]

