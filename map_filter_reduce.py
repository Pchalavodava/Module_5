import random
from functools import reduce

random_list: list[int] = [random.randint(0, 10) for x in range(10)]
print(f'Список случайных чисел {random_list}')


"""
Используйте map(), чтобы преобразовать список чисел в список их кубов, используя обычную функцию.

"""


def cubic_expansion(x: int) -> int:
    """
    Функция возведения числа x в третью степень
    :param x: int: Число для возведения куб
    :return: int: Число в кубе
    """
    return x ** 3


def get_cubed_numbers_list(input_list: list[int]) -> list[int]:
    """
    Функция возведения всех элементов списка в куб
    :param input_list: list[int]: Входящий список для возведения его элементов в третью степень
    :return: list[int]: Список чисел, возведенных в куб
    """
    cubed_numbers: list[int] = list(map(cubic_expansion, input_list))
    return cubed_numbers


print(f'Список чисел, возведенных в третью степень - {get_cubed_numbers_list(random_list)}')


"""
Используйте filter(), чтобы отобрать из списка чисел только те, которые делятся на 5,
используя обычную функцию.

"""


def division_by_five(x: int) -> bool:
    """
    Проверка деления числа на пять без остатка
    :param x: Число для деления на пять
    :return: bool: True, если число делится на пять без остатка, False - иначе
    """
    return x % 5 == 0


def get_division_by_five_list(input_list: list[int]) -> list[int]:
    """
    Функция фильтрации списка по условию, если элемент списка делится на пять
    :param input_list: list[int]: Список для фильтрации
    :return: list[int]: Список чисел, которые делятся на пять без остатка
    """
    filtered_numbers: list[int] = list(filter(division_by_five, input_list))
    return filtered_numbers


print(f'Список чисел, которые делятся на пять - {get_division_by_five_list(random_list)}')


"""
Используйте filter() и reduce(), чтобы найти произведение всех нечетных чисел в списке,
используя обычную функцию.

"""


def is_odd(x: int) -> bool:
    """
    Функция проверки на нечетное число
    :param x: int: Число для проверки на нечетность
    :return: bool: True - если число нечетное, False - иначе
    """
    return x % 2 != 0


def multiply(x: int, y: int) -> int:
    """
    Нахождение произведения двух заданных чисел
    :param x: int: Первое число для умножения
    :param y: int: Второе число для умножения
    :return: int: Произведение двух заданных чисел
    """
    return x * y


def multiply_odd_numbers(input_list: list[int]) -> int:
    """
    Функция произведения всех нечетных чисел из заданного списка
    :param input_list: list[int]: Входящий список для нахождения всех нечетных чисел в нем и дальнейшее
    произведение этих чисел
    :return: int: Произведение нечетных чисел из списка
    """
    odd_numbers_list: list[int] = list(filter(is_odd, input_list))
    product: int = reduce(multiply, odd_numbers_list)
    return product


print(f'Произведение всех нечетных чисел в заданном списке = {multiply_odd_numbers(random_list)}')