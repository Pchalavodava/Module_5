"""
Дан словарь учеников. Отсортировать учеников по возрасту.

"""


def sort_by_age(input_dict: dict[str, int]) -> list[tuple[str, int]]:
    """
    Сортировка словаря по значению (сортировка студентов по возрасту)
    :param input_dict: dict[str, int]: Словарь для сортировки
    :return: list[tuple[str, int]]: Список кортежей (отсортированных студентов по возрасту)
    """
    sorted_dict: list[tuple[str, int]] = sorted(input_dict.items(), key=lambda x: x[1])
    return sorted_dict


students_dict: dict[str, int] = {
 'Саша': 27,
 'Кирилл': 52,
 'Маша': 14,
 'Петя': 36,
 'Оля': 43,
}

print(sort_by_age(students_dict))

"""
Дан список с данными о росте и весе людей. Отсортировать их по индексу массы тела. 
Он вычисляется по формуле: 

Вес тела в килограммах/(Рост в метрах∗Рост в метрах)

"""


def calc(x: tuple[int, int]) -> int | float:
    """
    Расчет индекса массы тела. Формула: Вес тела в килограммах/(Рост в метрах∗Рост в метрах)
    :param x: Кортеж значений, где нулевой элемент - вес в килограммах, первый - рост в сантиметрах
    :return: int: Индекс массы тела
    """
    return round(x[0] / ((x[1]/100)*(x[1]/100)), 2)


def bmi_calculation(input_list: list[tuple[int, int]]) -> list[int]:
    """
    Применение формулы расчета ИМТ для каждого элемента в списке
    :param input_list: list[tuple[int, int]]: Список кортежей, где нулевой элемент - вес в килограммах,
    первый - рост в сантиметрах
    :return: list[int]: Список индексов массы тела
    """
    return list(map(calc, input_list))


def sort_by_bmi(input_list: list[tuple[int, int]]) -> list[int]:
    """
    Сортировка индексов массы тела по возрастанию
    :param input_list: Список кортежей, где нулевой элемент - вес в килограммах,
    первый - рост в сантиметрах
    :return: list[int]: Отсортированный список индексов массы тела
    """
    return sorted(bmi_calculation(input_list))


data: list[tuple[int, int]] = [
    (82, 191),
    (68, 174),
    (90, 189),
    (73, 179),
    (76, 184)
]

print(sort_by_bmi(data))

"""
Дан словарь учеников. Найти самого минимального ученика по возрасту

"""


def get_younger_student(students: list[dict[str, int]]) -> dict[str, int]:
    """
    Функция нахождения младшего студента
    :param students: list[dict[str, int]]: Список словарей (студентов), где каждый словарь - студент с ключами
    name и age
    :return: dict[str, int]: Младший студент. Словарь с наименьшим значением ключа age
    """
    return min(students, key=lambda student: student['age'])


students_list: list[dict[str, int]] = [
    {
        "name": "Саша",
        "age": 27,
    },
    {
        "name": "Кирилл",
        "age": 52,
    },
    {
        "name": "Маша",
        "age": 14,
    },
    {
        "name": "Петя",
        "age": 36,
    },
    {
        "name": "Оля",
        "age": 43,
    },
]

print(get_younger_student(students_list))