"""Компоновка дерева групп CLI приложения"""
import click

from omlb.cli.groups.homework import HomeworkTasksGroup


@click.group(help='Pavel Bass. OTUS Machine Learning Basic 2024')
def root_group():
    """Корневая группа CLI приложения"""

@root_group.group(name='hw', help='Домашние задания')
def homeworks_group():
    """Группа домашних заданий"""

# Группа домашнего задания 1
homeworks_group.add_command(HomeworkTasksGroup(name='1'))

# Группа домашнего задания 2
homeworks_group.add_command(HomeworkTasksGroup(name='2'))

# Группа домашнего задания 3
homeworks_group.add_command(HomeworkTasksGroup(name='3'))
