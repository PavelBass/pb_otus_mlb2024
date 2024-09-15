import pytest

from omlb.homeworks.hw1 import (
    task1,
    task2,
    task3,
    task4,
    task5,
)


@pytest.mark.parametrize(
    'value, output',(

        ('23456', '25436'),
        ('30789', '38709'),
    )
)
def test_task1__print_expected(value, output, mocker):
    # arrange
    mocked_input = mocker.patch('omlb.homeworks.hw1.input', return_value=value)
    mocked_print = mocker.patch('omlb.homeworks.hw1.print')

    # act
    task1()

    # assert
    mocked_print.assert_called_once_with(output)


@pytest.mark.parametrize(
    'days, output',(

        ('4', 'До отпуска осталось 0 выходных'),
        ('6', 'До отпуска осталось 1 выходных'),
        ('14', 'До отпуска осталось 4 выходных'),
    )
)
def test_task2__print_expected(days, output, mocker):
    # arrange
    mocked_input = mocker.patch('omlb.homeworks.hw1.input', return_value=days)
    mocked_print = mocker.patch('omlb.homeworks.hw1.print')

    # act
    task2()

    # assert
    mocked_print.assert_called_once_with(output)


@pytest.mark.parametrize(
    'data, output',(

        ('3, 4, 6', True),
        ('5, 7,8', False),
        ('4,5, 12', True),
        ('4,2,12', False),
    )
)
def test_task3__print_expected(data, output, mocker):
    # arrange
    mocked_input = mocker.patch('omlb.homeworks.hw1.input', return_value=data)
    mocked_print = mocker.patch('omlb.homeworks.hw1.print')

    # act
    task3()

    # assert
    mocked_print.assert_called_once_with(output)


@pytest.mark.parametrize(
    'data, output',(
        ('3', 'III'),
        ('15', 'XV'),
        ('234', 'CCXXXIV'),
    )
)
def test_task4__print_expected(data, output, mocker):
    # arrange
    mocked_input = mocker.patch('omlb.homeworks.hw1.input', return_value=data)
    mocked_print = mocker.patch('omlb.homeworks.hw1.print')

    # act
    task4()

    # assert
    mocked_print.assert_called_once_with(output)


@pytest.mark.parametrize(
    'data, output',(
        ('5.6', True),
        ('0.78', True),
        ('.78', True),
        ('.67.', False),
        ('5', True),
        ('-5.6', True),
        ('-0.78', True),
        ('-.78', True),
        ('-.67.', False),
        ('-5', True),
    )
)
def test_task5__print_expected(data, output, mocker):
    # arrange
    mocked_input = mocker.patch('omlb.homeworks.hw1.input', return_value=data)
    mocked_print = mocker.patch('omlb.homeworks.hw1.print')

    # act
    task5()

    # assert
    mocked_print.assert_called_once_with(output)

