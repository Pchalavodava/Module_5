"""Реализовать конвертер из csv в json формат:

[{column -> value}, ... , {column -> value}]

название столбца — значение (аналог DictReader из модуля csv).

Для csv формата принять

разделитель между значениями, по умолчанию ","

разделитель строк, по умолчанию "\n".

В результате распечатать json строку с отступами равными 4."""

import csv
import json


def create_python_object_from_csv(file: str) -> list[dict[str: str | int]]:
    """
    Формирование списка словарей из CSV-файл
    :param file: str: CSV-файл для обработки
    :return: list[dict[str: str | int]]: Список словарей, где ключи - поля таблицы csv, значения - строки таблицы csv
    """
    row_list: list = []
    dicts_from_csv: list = []
    with open(file, 'r', encoding='utf') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row:
                row_list.append(row)
        i: int = 1
        while i < len(row_list):
            dicts_from_csv.append(dict(zip(row_list[0], row_list[i])))
            i += 1
        return dicts_from_csv


def from_csv_to_json(file: str) -> str:
    """
    Конвертация csv-файла в строку json
    :param file: str: csv-файл для обработки
    :return: str: строка json
    """
    python_object_from_csv: list[dict[str: str | int]] = create_python_object_from_csv(file)
    json_data = json.dumps(python_object_from_csv, indent=4)
    return json_data


print(from_csv_to_json('prices_1.csv'))

# def decoding_json_object(json_obj):
#     json_data = from_csv_to_json(json_obj)
#     decoded = json.loads(json_data)
#     return decoded

# print(decoding_json_object('prices_1.csv'))
