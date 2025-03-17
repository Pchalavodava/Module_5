import csv
import json
from functools import reduce
from typing import Any

from cprint import cprint

students_json = 'student_list.json'

"""
Задание 0. Работа с json.
Считайте данные из файла student_list.json и преобразуйте в словарь students.

"""


def create_dict_from_json(json_file: str) -> dict[str, Any]:
    """
    Формирование словаря (списка студентов) из заданного файл json
    :param json_file: str: json-файл для формирования из него словаря
    :return: dict[str, dict[str]]: Словарь, где ключи - имена студентов, а значения - информация о них: возраст,
    изучаемые предметы и баллы по этим предметам
    """
    with open(json_file, 'r', encoding='utf-8') as j_file:
        return json.load(j_file)


students_dicts_from_json = create_dict_from_json(students_json)


"""
Задание 1: Средний балл по всем предметам
Напишите функцию get_average_score(), которая вычисляет средний балл по всем 
предметам для каждого студента в словаре students. Выведите результат в формате:

Средний балл для студента John: 85.0
Средний балл для студента Alice: 83.33333333333333
Средний балл для студента Michael: 85.0
Средний балл для студента Sophia: 90.66666666666667
Средний балл для студента Robert: 83.66666666666667

"""


def calculation_of_average_score(grades: dict[str, float]) -> float:
    """
    Расчет среднего балла по формуле: sum(grades) / len(grades)
    :param grades: dict[str, float]: Словарь оценок, где ключи - предметы, значения - баллы
    :return: float: Средний балл
    """
    return reduce(lambda x, y: x + y, grades.values()) / len(grades)


def add_average_score(students_dicts: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """
    Добавление среднего балла в словарь
    :param students_dicts: dict[str, dict[str]]: словарь студентов для добавления в него значений о средних баллах
    :return: dict[str, dict[str]]: Новый словарь студентов, включающий значения о среднем балле
    """
    for name, student_info in students_dicts.items():
        student_info['average_score'] = calculation_of_average_score(student_info['grades'])
    return students_dicts


students_dicts_with_average_score = add_average_score(students_dicts_from_json)


def print_average_score() -> None:
    """
    Функция вывода на консоль строки с информацией о студенте и его среднем балле
    """
    for name, info in students_dicts_with_average_score.items():
        cprint(f'Средний балл для студента {name}: {info['average_score']}', c='y')


print_average_score()


"""
Задание 2: Наилучший и худший студент
Напишите функции get_best_student() и get_worst_student(), которые находят студента с наилучшим и худшим средним баллом соответственно. Выведите их имена и средние баллы в следующем формате:

Наилучший студент: Sophia (Средний балл: 90.67)
Худший студент: Robert (Средний балл: 83.67)

"""


def get_best_student() -> tuple[str, dict[str, Any]]:
    """
    Функция нахождения наилучшего студента по его среднему баллу
    :return: tuple[str, dict]: Кортеж, где нулевой элемент - имя студента, первый - информация о нем
    """
    the_best_student = max(students_dicts_with_average_score.items(), key=lambda student: student[1]['average_score'])
    return the_best_student


def get_worst_student() -> tuple[str, dict[str, Any]]:
    """
    Функция нахождения худшего студента по его среднему баллу
    :return: tuple[str, dict]: Кортеж, где нулевой элемент - имя студента, первый - информация о нем
    """
    worst_student = min(students_dicts_with_average_score.items(), key=lambda student: student[1]['average_score'])
    return worst_student


best = get_best_student()
worst = get_worst_student()
cprint(f'Наилучший студент: {best[0]} (Средний балл: {best[1]['average_score']})\n'
       f'Наихудший студент: {worst[0]} (Средний балл: {worst[1]['average_score']})', c='g')


"""
Задание 3: Поиск по имени
Напишите функцию find_student(name), которая принимает имя студента в качестве аргумента 
и выводит информацию о нем, если такой студент есть в словаре students. В противном случае, 
выведите сообщение "Студент с таким именем не найден".

Пример:

find_student("John")
Имя: John
Возраст: 20
Предметы: ['Math', 'Physics', 'History']
Оценки: {'Math': 95, 'Physics': 88, 'History': 72}

"""


def find_student(name: str) -> str:
    """
    Функция поиска студента по имени. Если студент найден, то возвращается строка с информацией о нем,
    иначе - сообщение (строка), что такой студент не найден
    :param name: str: Имя студента для поиска
    :return: str: Строковая информация о студенте или же сообщение, что такого студента нет
    """
    found_student = students_dicts_from_json.get(name.title(), 'Студент с таким именем не найден')
    if isinstance(found_student, dict):
        return (f'Имя: {name.title()} \nВозраст: {found_student['age']} \nПредметы: {found_student['subjects']} \n'
                f'Оценки: {found_student['grades']}')
    return found_student


cprint(find_student('john'), c='b')


"""
Отсортируйте студентов по их среднему баллу в порядке убывания. Выведите имена студентов 
и их средние баллы в следующем формате:

Сортировка студентов по среднему баллу:
Sophia: 90.67
Michael: 85.0
John: 85.0
Alice: 83.33
Robert: 83.67

"""


def sort_by_grade(students: dict[str, dict[str, Any]]) -> list[tuple[str, dict[str, Any]]]:
    """
    Функция сортировки словарей по убыванию по значению 'average_score'.
    :param students: dict[str, dict[str, Any]]: Словарь студентов, с уже рассчитанным средним баллом
    :return: list[tuple[str, dict[str, Any]]]: Словарь кортежей студентов, где нулевой элемент - имя студента,
    первый - информация о нем
    """
    sorted_list = sorted(students.items(), key=lambda x: x[1]['average_score'], reverse=True)
    return sorted_list


def print_sorted_students_by_average_score() -> None:
    """
    Вывод на печать имени студента и его среднего балла
    :return: None
    """
    student_list = sort_by_grade(students_dicts_with_average_score)
    cprint('Сортировка студентов по среднему баллу:', c='m')
    for student in student_list:
        cprint(f'{student[0]}: {student[1]['average_score']}', c='m')


print_sorted_students_by_average_score()


"""
Преобразуйте словарь в список словарей данного формата
students = [
    {
        'name': 'John',
        'age': 20,
        'subjects': ['Math', 'Physics', 'History', 'Chemistry', 'English'],
        'grades': {'Math': 95, 'Physics': 88, 'History': 72, 'Chemistry': 84, 'English': 90}
    },
    {
        'name': 'Alice',
        'age': 19,
        'subjects': ['Biology', 'Chemistry', 'Literature', 'Math', 'Art'],
        'grades': {'Biology': 80, 'Chemistry': 92, 'Literature': 78, 'Math': 88, 'Art': 86}
    },
    {
        'name': 'Michael',
        'age': 22,
        'subjects': ['Computer Science', 'English', 'Art', 'History', 'Economics'],
        'grades': {'Computer Science': 87, 'English': 78, 'Art': 90, 'History': 82, 'Economics': 75}
    },
    # информация о других студентах здесь
]

"""


def add_name_to_value(student: tuple[str, dict[Any]]) -> dict[str, Any]:
    """
    Функция добавления имени в информацию о студенте (создание нового словаря, состоящего из словаря
    информации о студенте и с добавлением в него имени (нулевого элемента кортежа) на первое место)
    :param student: tuple[str, dict[Any]]: Кортеж, где нулевой элемент - имя студента, первый -
    словарь информации о нем
    :return: dict[str, Any]: Новый словарь информации о студенте с новым объектом - 'name'
    """
    dict_with_name = {'name': student[0]}
    dict_with_name.update(student[1])
    return dict_with_name


def create_dicts_with_name() -> list[dict[str, Any]]:
    """
    Функция применения функции 'add_name_to_value' к каждому объекту словаря 'students_dicts_from_json'
    :return: list[dict[str, Any]: Список словарей студентов
    """
    return list(map(add_name_to_value, students_dicts_from_json.items()))


print(create_dicts_with_name())


"""
Задание 6. Сформируйте csv
Сформируйте файл в формате csv следующего вида

Заголовки: name,age,grade - имя, возраст и средний балл студента 

Данные: 

John, 20, 85.0
Alice, 19, 83.3
Michael, 22, 85.0
...

"""

fields_names = ['name', 'age', 'average_score']


def filter_dict(element: dict[str, Any]) -> dict[str, Any]:
    """
    Функция удаления объектов словаря, ключи которых не соответствуют заданному списку
    :param element: dict[str, Any]: Словарь (студент)
    :return: dict[str, Any]: Отфильтрованный словарь по нужным полям
    """
    for key, value in list(element.items()):
        if key not in fields_names:
            element.pop(key)
    return element


def dict_by_fields_names() -> list[dict[str, Any]]:
    """
    Функция применения функции 'filter_dict' к каждому объекту списка словарей студентов, сформированного
    с помощью функции 'create_dicts_with_name'
    :return: list[dict[str, Any]]: Список словарей студентов с ключами из списка 'fields_names'
    """
    return list(map(filter_dict, create_dicts_with_name()))


def append_to_csv(csv_file: str, student_dict: dict[str, Any]) -> None:
    """
    Функция добавления словаря в файл csv
    :param csv_file: str: Файл для записи
    :param student_dict: dict[str, Any]]: Словарь (студент) для записи в csv-файл
    :return: None
    """
    with open(csv_file, 'a', encoding='utf-8') as csv_f:
        writer = csv.DictWriter(csv_f, fieldnames=fields_names)
        writer.writerow(student_dict)


def write_student_to_csv(csv_file: str) -> None:
    """
    Функция применения функции 'append_to_csv' к каждому объекту списка студентов, сформированного функцией
    'dict_by_field_names'
    :param csv_file: str: csv-файл для записи
    :return: None
    """
    open(csv_file, 'w').close()
    for student in dict_by_fields_names():
        append_to_csv(csv_file, student)


write_student_to_csv('csv_students.csv')
