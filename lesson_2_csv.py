import csv

"""
Exercise_0
"""

# Чтение данных из csv-файла
with open('данные.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open('данные.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    print(list(reader))

# Запись данных в csv-файл
data = [
    ['Имя', 'Возраст', 'Город'],
    ['Анна', '25', 'Москва'],
    ['Петр', '30', 'Санкт-Петербург'],
    ['Мария', '28', 'киев']
]
with open('новые_данные.csv', 'w', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(data)

# Запись и чтение данных с использованием словаря (csv-файл с заголовками)
data = [
    {'Имя': 'Анна', 'Возраст': '25', 'Город': 'Москва'},
    {'Имя': 'Петр', 'Возраст': '30', 'Город': 'Санкт-Петербург'},
    {'Имя': 'Мария', 'Возраст': '28', 'Город': 'Киев'}
]

with open('данные_с_заголовками.csv', 'w', encoding='utf-8') as csvfile:
    fieldnames = ['Имя', 'Возраст', 'Город']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

with open('данные_с_заголовками.csv', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Имя'], row['Возраст'], row['Город'])

with open('новые_данные.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print(row)


"""
Exercise_1
Имеется текстовый файл prices.txt с информацией о заказе из интернет магазина. 
В нем каждая строка с помощью символа табуляции \t разделена на три колонки: 
наименование товара; количество товара (целое число); цена (в рублях) товара за 1 шт. (целое число). 
Напишите программу, преобразующую данные из txt в csv.
"""


def get_list(file: str) -> list[dict[str, str]]:
    """
    Получение из текстового файла списка словарей
    :param file: str: Текстовый файл, который необходимо преобразовать в список
    :return: list[dict[str, str]]: Список словарей, где ключи - заголовки таблицы, значения - значения колонок
    """
    list_from_txt = []
    goods_dicts = []
    with open(file, encoding='utf-8') as txt_file:
        for line in txt_file:
            # Здесь совсем не уверена насчет разбития по столбцам по табуляции.
            # Долго искала инфо и ничего нашла, но методом проб и ошибок пришла к тому, что разбилось по '\\t'
            list_from_txt.append(line.strip().split('\\t'))
        i = 1
        while i < len(list_from_txt):
            goods_dicts.append(dict(zip(list_from_txt[0], list_from_txt[i])))
            i += 1
        return goods_dicts


def convert_to_csv(file: str, new_file: str) -> None:
    """
    Функция преобразования txt-файла в csv-файл.
    :param new_file: str: Название нового файла csv, в который будет конвертирован файл txt
    :param file: str: Файл txt для конвертации
    :return: None
    """
    goods_list = get_list(file)
    keys = []
    for dicts in goods_list:
        for key in dicts.keys():
            if key not in keys:
                keys.append(key)

    with open(new_file, 'w', encoding='utf-8') as csv_file:
        field_names = keys
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(goods_list)


convert_to_csv('prices.txt', 'prices.csv')


"""
Exercise_2
Имеется файл prices.csv (сформированный в прошлом задании) с информацией о заказе из интернет магазина. 
В нем каждая строка содержит три колонки: наименование товара; количество товара (целое число); 
цена (в рублях) товара за 1 шт. (целое число). Напишите программу, подсчитывающую общую стоимость заказа.
"""


def get_list_dicts(file: str) -> list[dict[str, str]]:
    """
    Формирование словаря из поданного для обработки csv-файла
    :param file: str: CSV-файл с входящими данными
    :return: list[dict[str, str]]: Список словарей, где ключи - поля таблицы, значения - строки
    """
    rows_list = []
    goods_list = []
    with open(file, encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row:
                rows_list.append(row)
        i = 1
        while i < len(rows_list):
            goods_list.append(dict(zip(rows_list[0], rows_list[i])))
            i += 1
    return goods_list


def get_total_price(file: str) -> int:
    """
    Расчет полной стоимости заказа
    :param file: str: Файл для обработки данных
    :return: int: Стоимость заказа
    """
    goods_list = get_list_dicts(file)
    total_price = 0
    for goods in goods_list:
        try:
            price_of_goods = int(goods['Количество товара']) * int(goods['Цена за 1 шт.'])
        except Exception:
            price_of_goods = 0
        total_price += price_of_goods
    return total_price


total = get_total_price('prices.csv')
print(f'Общая стоимость заказа составляет {total} рублей')
