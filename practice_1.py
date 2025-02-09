import json
import csv
from datetime import datetime
from typing import Union

from cprint import cprint


def read_csv(csv_file):
    file = open(csv_file, 'r', encoding='utf-8')
    reader = csv.reader(file)
    return reader


"""Задание 1: Работа с JSON файлом
Задача:
Студентам предлагается JSON файл с данными о студентах. Необходимо создать программу, которая проведет
анализ этих данных и выведет информацию на экран.

Прочитать данные из файла students.json.
Определить общее количество студентов в файле.
Найти студента с самым высоким возрастом и вывести его данные (имя, возраст, город).
Определить количество студентов, изучающих определенный предмет (например, Python)."""


def get_list_from_json(file: str) -> list[dict[str, Union[str, int]]]:
    """
    Конвертация файла json в объект Python (список)
    :param file: str: Файл json для обработки
    :return: list[dict[str, str | int]]: Список словарей (студентов)
    """
    with open(file, 'r', encoding='utf-8') as json_file:
        list_from_json: list[dict[str, Union[str, int]]] = json.load(json_file)
        return list_from_json


def get_numbers_of_students(students: list[dict[str, Union[str, int]]]) -> int:
    """
    Получение общего количества студентов (общее количество элементов в списке)
    :param students: list[dict[str, str | int]]: Список студентов
    :return: int: Общее количество студентов (длина списка)
    """
    return len(students)


def get_max_age_student(students: list[dict[str, Union[str, int]]]) -> tuple[str, int, str]:
    """
    Получение самого старшего студента
    :param students: list[dict[str, str | dict]]: Список студентов для поиска старшего из них
    :return: tuple[str, int, str]: Кортеж из имени, возраста и города старшего студента
    """
    max_age: int = max(student.get('возраст') for student in students)
    older_student: list[dict[str, Union[str, int]]] = [student for student in students if student.get('возраст') == max_age]
    for max_age_student in older_student:
        return max_age_student.get('имя'), max_age_student.get('возраст'), max_age_student.get('город')


def get_students_by_discipline(students: list[dict[str, Union[str, int]]]) -> dict[str, int]:
    """
    Получение словаря предметов, где ключ - это название предмета, значение - количество студентов,
    изучающих данный предмет
    :param students: list[dict[str, str | int]]: Список студентов для обработки
    :return: dict[str, int]: Словарь предметов, где ключи - изучаемые дисциплины, значения - количество
    студентов, их изучающих
    """
    dict_of_disciplines: dict[str, int] = {}
    for student in students:
        for discipline in student['предметы']:
            if discipline not in dict_of_disciplines.keys():
                dict_of_disciplines[discipline] = 1
            else:
                dict_of_disciplines[discipline] += 1
    return dict_of_disciplines


def file_analysis(file: str) -> None:
    """
    Вывод анализа данных по выбранному json-файлу
    :param file: str: json-файл для обработки
    :return: None
    """
    list_of_students: list[dict[str, Union[str, int]]] = get_list_from_json(file)
    total_students: int = get_numbers_of_students(list_of_students)
    older_student: tuple[str, int, str] = get_max_age_student(list_of_students)
    students_by_disciplines: dict[str, int] = get_students_by_discipline(list_of_students)
    cprint(f'Общее количество студентов - {total_students}\n'
           f'Самый старший студент - это {older_student[0]}, из города {older_student[2]}, которому '
           f'{older_student[1]} лет\n'
           f'Количество студентов, изучающих определенный предмет: {students_by_disciplines}', c='b')


file_analysis('students.json')

"""Задание 2: Работа с CSV файлом
Задача:
Предоставить студентам файл в формате CSV с данными о продажах в компании. Задача - обработать этот 
файл и получить полезную информацию.

Считать данные из файла sales.csv.
Подсчитать общую сумму продаж за весь период.
Определить продукт с самым высоким объемом продаж и вывести его на экран.
Разделить данные на категории по месяцам и вывести общую сумму продаж для каждого месяца."""


def get_goods_list(csv_file: str) -> list[dict[str, Union[str, int]]]:
    """
    Формирование списка словарей товаров из csv-файла
    :param csv_file: str: csv-файл для обработки
    :return: list[dict[str, str | int]]: Список словарей (товаров)
    """
    goods_list: list[dict[str, Union[str, int]]] = []
    # with open(csv_file, 'r', encoding='utf-8') as file:
    #     reader = csv.reader(file)
    reader = read_csv(csv_file)
    reader = list(map(lambda y: list(map(lambda x: x.strip(), y)), reader))
    i: int = 1
    while i < len(reader):
        goods_list.append(dict(zip(reader[0], reader[i])))
        i += 1
    return goods_list


def get_total_sales_amount(sales: list[dict[str, Union[str, int]]]) -> int:
    """
    Расчет общей суммы продаж по всем товарам
    :param sales: list[dict[str, str | int]]: Список товаров
    :return: int: общая сумма проданных товаров в рублях
    """
    total: int = 0
    for goods in sales:
        total += int(goods.get('Сумма'))
    return total


def get_most_popular_product(sales: list[dict[str, Union[str, int]]]) -> tuple[str, int]:
    """
    Поиск продукта с наибольшим объемом продаж
    :param sales: list[dict[str, str | int]]: Список товаров
    :return: tuple[str, int]: Кортеж из названия товара и общим объемом продаж по нему
    """
    goods_dict: dict[str, int] = {}
    for goods in sales:
        if goods.get('Продукт') not in goods_dict:
            goods_dict[goods.get('Продукт')] = int(goods.get('Сумма'))
        else:
            goods_dict[goods.get('Продукт')] += int(goods.get('Сумма'))
    max_sales = max(x for x in goods_dict.values())
    most_popular_product = next(key for key, value in goods_dict.items() if value == max_sales)
    return most_popular_product, goods_dict[most_popular_product]


def sales_by_month(sales: list[dict[str, Union[str, datetime]]]) -> dict[str, int]:
    """
    Формирование словаря продаж по месяцам
    :param sales: list[dict[str, str | datetime]]: Список товаров для обработки
    :return: dict[str, int]: Словарь продаж по месяцам, где ключ - месяц, значение - общие продажи по
    данному месяцу
    """
    month_sales: dict[str, int] = {}
    for date in sales:
        date['Дата']: datetime = datetime.strptime(date.get('Дата'), '%Y-%m-%d')
        if date.get('Дата').strftime('%B') not in month_sales:
            month_sales[date.get('Дата').strftime('%B')] = int(date.get('Сумма'))
        else:
            month_sales[date.get('Дата').strftime('%B')] += int(date.get('Сумма'))
    return month_sales


def file_analysis(file: str) -> None:
    """
    Вывод анализа по товарам
    :param file: str: Входящий csv-файл для обработки
    :return: None
    """
    goods_list: list[dict[str, Union[str, int]]] = get_goods_list(file)
    total_sales: int = get_total_sales_amount(goods_list)
    most_popular_product: tuple[str, int] = get_most_popular_product(goods_list)
    month_sales: dict[str, int] = sales_by_month(goods_list)
    cprint(f'Общая сумма продаж по всем продуктам за все месяца составила {total_sales} рублей,\n'
           f'Продукт с самым высоким объемом продаж - это {most_popular_product[0]}, который был продан'
           f'на сумму {most_popular_product[1]} рублей,\n'
           f'Продажи по месяцам составили: {month_sales}', c='g')


file_analysis('sales.csv')

"""Задание 3: Комбинированная работа с JSON и CSV
Задача:
Предоставить студентам два файла - JSON с информацией о сотрудниках и CSV с данными о их 
производительности. Задача - соединить эти данные для анализа.

Считать данные из файлов employees.json и performance.csv.
Сопоставить данные о производительности каждого сотрудника с их соответствующей информацией из JSON файла.
Определить среднюю производительность среди всех сотрудников и вывести ее.
Найти сотрудника с наивысшей производительностью и вывести его имя и показатель производительности."""


def get_employees_list(json_file: str) -> list[dict[str, Union[str, int]]]:
    """
    Конвертация файла json в список сотрудников
    :param json_file: str: json-файл для обработки
    :return: list[dict[str, str | int]]
    """
    with open(json_file, 'r', encoding='utf-8') as file:
        data: list[dict[str, Union[str, int]]] = json.load(file)
    return data


def get_performance_list(csv_file: str) -> list[dict[str, Union[str, int]]]:
    """
    Получение списка производительностей по каждому сотруднику
    :param csv_file: str: csv_файл для обработки
    :return: list[dict[str, str | dict]]
    """
    performance_lists: list[dict[str, Union[str, int]]] = []
    # with open(csv_file, 'r', encoding='utf-8') as file:
    #     reader = csv.reader(file)
    reader = read_csv(csv_file)
    reader = list(map(lambda y: list(map(lambda x: x.strip(), y)), reader))
    i = 1
    while i < len(reader):
        performance_lists.append(dict(zip(reader[0], reader[i])))
        i += 1
    return performance_lists


def get_employees_performance(employees_list: list[dict[str, Union[str, int]]],
                              performance_list: list[dict[str, Union[str, int]]]) -> list[dict[str, Union[str, int]]]:
    """
    Получение списка сотрудников с добавлением производительности посредством слияния словарей по
    id-номеру сотрудника
    :param employees_list: list[dict[str, str | int]]: Список сотрудников
    :param performance_list: list[dict[str, str | int]]: Список производительностей
    :return: list[dict[str, str | int]]: Список словарей, полученный слиянием словарей по id сотрудника
    """
    for employee in employees_list:
        for performance in performance_list:
            if int(employee['id']) == int(performance['employee_id']):
                employee['производительность'] = int(performance['performance'])
    return employees_list


def get_average_performance(employees: list[dict[str, Union[str, int]]]) -> float:
    """
    Определение средней производительности всех сотрудников
    :param employees: list[dict[str, str | int]]: Список сотрудников для обработки
    :return: float: Средняя производительность всех сотрудников
    """
    total_performance: int = sum(employee['производительность'] for employee in employees)
    try:
        average_performance: float = total_performance / len(employees)
        return average_performance
    except ZeroDivisionError:
        print('В списке нет ни одного сотрудника')


def get_max_performance(employees: list[dict[str, Union[str, int]]]) -> tuple[str, int]:
    """
    Получение сотрудника с наибольшей производительностью
    :param employees: list[dict[str, str | int]]: Список сотрудников
    :return: str: Имя наиболее производительного сотрудника
    """
    max_performance: int = max(employee.get('производительность') for employee in employees)
    the_best_employee: list[dict[str, Union[str, int]]] = [employee for employee in employees if
                                                     employee['производительность'] == max_performance]
    for name in the_best_employee:
        return name.get('имя'), name.get('производительность')


def performance_analysis(json_file: str, csv_file: str) -> None:
    """
    Вывод анализа производительности сотрудников
    :param json_file: str: Входящий json-файл со списком сотрудников
    :param csv_file: Входящий csv-файл со списком производительностей сотрудников
    :return: None
    """
    employees: list[dict[str, Union[str, int]]] = get_employees_list(json_file)
    performance: list[dict[str, Union[str, int]]] = get_performance_list(csv_file)
    employees_performance: list[dict[str, Union[str, int]]] = get_employees_performance(employees, performance)
    average_performance: float = get_average_performance(employees_performance)
    the_best_employee: tuple[str, int] = get_max_performance(employees_performance)
    cprint(f'Средняя производительность всех сотрудников составляет {average_performance}\n'
           f'Сотрудник с наилучшей производительностью - это {the_best_employee[0]} с производительностью '
           f'{the_best_employee[1]}', c='y')


performance_analysis('employees.json', 'performance.csv')


