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
        return [name[4:] for name in dir(self.module) if name.startswith('task')]

    def get_command(self, _: click.Context, name: str) -> Callable[..., click.Command]:
        """Получение задачи по номеру"""
        function = getattr(self.module, f'task{name}')
        command_help = function.__doc__
        return self.command(help=command_help)(function)

