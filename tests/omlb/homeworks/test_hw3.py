import pytest

from omlb.homeworks.hw3 import (
    task1,
    task2,
    task3,
    #task4,
    #task5,
)


@pytest.mark.parametrize(
    'value, expected',(
        ('otus_course', 'OtusCourse'),
        ('PythonIsTheBest', 'python_is_the_best'),
    )
)
def test_task1__print_expected(value, expected, mocker):
    # arrange
    mocked_input = mocker.patch('omlb.homeworks.hw3.input', return_value=value)
    mocked_print = mocker.patch('omlb.homeworks.hw3.print')

    # act
    task1()

    # assert
    mocked_print.assert_called_once_with(expected)


@pytest.mark.parametrize(
    'value, expected',(
        ('29.02.2000', True),
        ('29.02.2001', False),
        ('31.04.1962', False),
    )
)
def test_task2__print_expected(value, expected, mocker):
    # arrange
    mocked_input = mocker.patch('omlb.homeworks.hw3.input', return_value=value)
    mocked_print = mocker.patch('omlb.homeworks.hw3.print')

    # act
    task2()

    # assert
    mocked_print.assert_called_once_with(expected)


@pytest.mark.parametrize(
    'value, expected',(
        (17, True),
        (20, False),
        (23, True),
    )
)
def test_task3__print_expected(value, expected, mocker):
    # arrange
    mocked_input = mocker.patch('omlb.homeworks.hw3.input', return_value=value)
    mocked_print = mocker.patch('omlb.homeworks.hw3.print')

    # act
    task3()

    # assert
    mocked_print.assert_called_once_with(expected)
