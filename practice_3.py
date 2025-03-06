import csv
import itertools
import os

"""Проект: Генератор комбинаций карт
Цель:
Написать программу, которая создает все возможные комбинации из заданного количества карт
(от 1 до 52) в стандартной колоде.

Шаги:
Создание колоды:

Сгенерируйте список всех карт в стандартной колоде.
Генерация комбинаций:

Используйте модуль itertools, чтобы получить все комбинации из заданного числа карт.
Вывод результатов:

Выведите все комбинации на экран или сохраните их в файл для последующего использования."""


def generating_deck_card(cards: list[str], suits: list[str]) -> list[str]:
    """
    Генерация колоды игральных карт из названия карты и мастей
    :param cards: list[str]: Список названий карт
    :param suits: list[str]: Список мастей
    :return: list[str]: Список из 52 игральных карт, сформированный их двух списков: названия карт, масти карт
    """
    deck: list[tuple[str, str]] = list(itertools.product(cards, suits))
    deck: list[str] = list(map(lambda x: str(x[0]) + ' ' + x[1], deck))
    # print(len(deck))
    return list(deck)


def write_to_csv(file: str, row: list[str]) -> None:
    """
    Запись строки в файл
    :param file: str: Файл для добавления
    :param row: list[str]: Строка, которую необходимо добавить
    :return: None
    """
    if not os.path.exists(file):
        open(file, 'w').close()
    with open(file, 'a', encoding='utf-8') as csv_f:
        writer = csv.writer(csv_f)
        writer.writerow(row)


def clear_file(file: str) -> None:
    """
    Очищение файла, если он существует
    :param file: str: Файл для очистки
    :return: None
    """
    if os.path.exists(file):
        open(file, 'w').close()


def get_cards_combinations(deck: list[str], len_comb: int, file) -> None:
    """
    Подготовка файла к записи (очищение содержимого файла).
    Получение всех возможных комбинаций карт заданного размера и запись их в очищенный csv-файл
    :param file: str: Файл для записи в него комбинаций карт
    :param deck: list[str]: Список карт (игральная колода из 52 карт)
    :param len_comb: int: Длина возможных комбинаций карт
    :return: None
    """
    clear_file(file)
    for combination in itertools.combinations(deck, len_comb):
        write_to_csv(file, combination)


card_suits: list[str] = ['Пики', 'Черви', 'Крести', 'Бубны']
card_names: list[str] = ['Двойка', 'Тройка', 'Четвёрка', 'Пятёрка', 'Шестёрка', 'Семёрка',
                         'Восьмёрка', 'Девятка', 'Десятка', 'Валет', 'Дама', 'Король', 'Туз']

file_to_write = 'playing_cards_combinations.csv'

get_cards_combinations(generating_deck_card(card_names, card_suits), 1, file_to_write)
