import importlib
from collections.abc import Callable
from functools import cached_property
from types import ModuleType

import click


class HomeworkTasksGroup(click.Group):
    """Группа отдельного домашнего задания

    Представляет набор выполненных задач,
    определенных в модуле `omlb.homeworks.hw{self.name}`.
    Реализованные задачи подгружаются из модуля налету.
    """

    @property
    def help(self) -> str:
        """Описание домашнего задания"""
        return f'Домашнее задание {self.name}'

    @help.setter
    def help(self, _: str) -> None:
        """Установка описания домашнего задания
        click устанавливает описание из переданных параметров,
        переопределяем это поведение в пользу динамического
        property, описанного выше
        """
        pass

    @cached_property
    def module(self) -> ModuleType:
        """Модуль с заданиями

        Returns:
            Модуль с заданиями

        Raises:
            ModuleNotFoundError: если модуль не найден
        """
        return importlib.import_module(f'omlb.homeworks.hw{self.name}')

    def list_commands(self, _: click.Context) -> list[str]:
        """Список выполненных задач из домашнего задания, он же список команд"""
        return [name for name in dir(self.module) if name.startswith('task')]

    def get_command(self, _: click.Context, name: str) -> Callable[..., click.Command] | None:
        """Получение команды выполнения задачи по имени задачи"""
        try:
            function = getattr(self.module, name)
        except AttributeError:
            return None
        command_help = function.__doc__
        click.echo(command_help)
        return self.command(help=command_help)(function)

