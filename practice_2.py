import random
from collections import Counter, namedtuple, defaultdict, deque
from typing import Any

from cprint import cprint

"""Задание 1: Анализ списка чисел с помощью Counter.
Сгенерируйте случайный список чисел.
Используйте Counter, чтобы подсчитать количество уникальных элементов в списке.
Найдите три наиболее часто встречающихся элемента в списке и выведите их с количеством вхождений."""


def create_random_list() -> list[int]:
    """
    Формирование списка случайных чисел от 0 до 10 длинной от 10 до 30.
    :return: list[int]: Список случайных чисел
    """
    random_list: list[int] = []
    len_list: int = random.randint(10, 30)
    for _ in range(len_list):
        num: int = random.randint(0, 10)
        random_list.append(num)
    return random_list


def get_repetition_dict(num_list: list[int]) -> Counter[int]:
    """
    Формирование словаря повторений, где ключ - объект списка, значение - количество повторений
    :param num_list: list[int]: Список чисел для обработки
    :return: Counter[int]: Словарь повторений
    """
    counter: Counter[int] = Counter(num_list)
    return counter


def get_unique_nums(numbers: Counter[int]) -> list[tuple[int, int]]:
    """
    Формирование списка кортежей из уникальных чисел, где нулевой элемент - число из объекта Counter,
    а первый - количество его повторений
    :param numbers: Counter[int]: Список повторений чисел
    :return: list[tuple[int, int]]: Список кортежей из уникальных чисел
    """
    unique_numbers: list[tuple[int, int]] = []
    for key, value in numbers.items():
        if value == 1:
            unique_numbers.append((key, value))
    return unique_numbers


def get_most_common_numbers(numbers: Counter[int]) -> list[tuple[int, int]]:
    """
    Получение списка кортежей из трех наиболее повторяющихся чисел, где нулевой элемент - число, первый -
    количество его повторений
    :param numbers: Counter[int]: Список повторений чисел
    :return: list[tuple[int, int]]: Список кортежей наиболее повторяющихся чисел
    """
    most_common: list[tuple[int, int]] = numbers.most_common(3)
    return most_common


def analysis_list_of_numbers() -> None:
    """
    Вывод результатов анализа списка случайных чисел
    :return: None
    """
    list_of_numbers: list[int] = create_random_list()
    repetition_dict: Counter[int] = get_repetition_dict(list_of_numbers)
    unique_nums: list[tuple[int, int]] = get_unique_nums(repetition_dict)
    common_nums: list[tuple[int, int]] = get_most_common_numbers(repetition_dict)
    print(f'Список для обработки: {list_of_numbers}\n'
          f'Список уникальных чисел: {unique_nums}\n'
          f'Список трех наиболее повторяющихся чисел: {common_nums}')


analysis_list_of_numbers()

"""Задание 2: Работа с именованными кортежами.
Создайте именованный кортеж Book с полями title, author, genre.
Создайте несколько экземпляров Book.
Выведите информацию о книгах, используя атрибуты именованных кортежей."""


def create_named_tuple() -> [str, list[str]]:
    """
    Создание именованного кортежа 'Book' с атрибутами 'title', 'author', 'genre'
    :return: [str, list[str]]: Именованный кортеж Book
    """
    Book = namedtuple('Book', ['title', 'author', 'genre'])
    return Book


def create_instance_of_tuple(created_tuple: [str, list[str]]) -> [str, list[str]]:
    book1: [str, list[str]] = created_tuple(title='Война и мир', author='Лев Толстой', genre='Роман')
    book2: [str, list[str]] = created_tuple(title='1984', author='Джордж Оруэлл', genre='Антиутопия')
    book3: [str, list[str]] = created_tuple(title='Лолита', author='Владимир Набоков', genre='Роман')
    return book1, book2, book3


def get_books_info() -> None:
    """
    Вывод информации из именованных кортежей
    :return: None
    """
    book_object: [str, list[str]] = create_named_tuple()
    books: [str, list[str]] = create_instance_of_tuple(book_object)
    cprint('Полная информация о книгах:', c='b')
    for book in books:
        cprint(f'    Автор: {book.author}, Название книги: {book.title}, Жанр: {book.genre}', c='b')


get_books_info()

"""Задание 3: Работа с defaultdict.
Создайте defaultdict с типом данных list.
Добавьте несколько элементов в словарь, используя ключи и значения.
Выведите содержимое словаря, где значения - это списки элементов с одинаковыми ключами."""


def create_defaultdict() -> defaultdict:
    """
    Создание defaultdict с типом данных list
    :return: defaultdict: defaultdict с типом данных list
    """
    ddict: defaultdict = defaultdict(list)
    return ddict


def write_to_ddict(ddict: defaultdict) -> defaultdict:
    """
    Добавление элементов в словарь
    :param ddict: defaultdict: defaultdict с типом данных list
    :return: defaultdict с добавлением в него нескольких элементов
    """
    ddict['apple'] = ['red', 'yellow', 'green']
    ddict['pear'] = ['yellow', 'green']
    ddict['banana'] = ['yellow']
    ddict['avocado'] = ['green']
    return ddict


def create_new_list_from_defaultdict(ddict: defaultdict) -> dict[str, list[str]]:
    """
    Формирование словаря, где значения - это списки элементов с одинаковыми ключами.
    :param ddict: Defaultdict: defaultdict для формирования из него словаря
    :return: dict[str, list[str]]: Словарь, где значения - это списки элементов с одинаковыми ключами.
    """
    new_dict: dict[str, list[str]] = {}
    for key, value in ddict.items():
        for val in value:
            if val not in new_dict.keys():
                new_dict[val] = [key]
            else:
                new_dict[val].append(key)
    return new_dict


def output_information_from_ddict() -> None:
    """
    Вывод на консоль обработанной информации
    :return: None
    """
    ddict: defaultdict = create_defaultdict()
    old_ddict: defaultdict = write_to_ddict(ddict)
    output_dict: dict[str, list[str]] = create_new_list_from_defaultdict(ddict)
    cprint(f'Словарь из которого необходимо сформировать словарь, где значения - это списки элементов '
           f'с одинаковыми ключами:\n{old_ddict}\n'
           f'Результат: {output_dict}', c='y')


output_information_from_ddict()

"""Задание 4: Использование deque для обработки данных.
Создайте deque и добавьте в него элементы.
Используйте методы append, appendleft, pop и popleft для добавления и удаления элементов из deque.
Проверьте, как изменяется deque после каждой операции."""


def create_new_deque() -> deque:
    """
    Создание новой двусторонней очереди
    :return: deque: Двусторонняя очередь
    """
    queue: deque = deque([1, 2, 3])
    return queue


def add_to_end(my_deque: deque, element: Any) -> deque:
    """
    Добавление в конец нового элемента
    :param my_deque: deque: Очередь, куда необходимо добавить элемент
    :param element: int: Элемент, который необходимо добавить
    :return: deque: Новая очередь
    """
    my_deque.append(element)
    return my_deque


def add_to_head(my_deque: deque, element: Any) -> deque:
    """
    Добавление нового элемента в начало
    :param my_deque: deque: Очередь, куда необходимо добавить новый элемент
    :param element: int: Элемент, который необходимо добавить
    :return: deque: Новая очередь
    """
    my_deque.appendleft(element)
    return my_deque


def delite_last_element(my_deque: deque) -> deque:
    """
    Удаление последнего элемента из двусторонней очереди
    :param my_deque: deque: Очередь, из которой необходимо удалить последний элемент
    :return: deque: Новая очередь
    """
    my_deque.pop()
    return my_deque


def delite_first_element(my_deque: deque) -> deque:
    """
    Удаление первого элемента из очереди
    :param my_deque: deque: Очередь до удаления первого элемента
    :return: Очередь после удаления первого элемента
    """
    my_deque.popleft()
    return my_deque


def try_add_pop_operations() -> None:
    """
    Функция добавления и удаления элементов из двусторонней очереди
    :return: None
    """
    queue: deque = create_new_deque()
    add_to_end(queue, 1)
    print(f'После добавление в конец, дек стал {queue}')
    add_to_head(queue, 2)
    print(f'После добавление в начало, дек стал {queue}')
    delite_last_element(queue)
    print(f'После удаления последнего элемента, дек стал {queue}')
    delite_first_element(queue)
    print(f'После удаления последнего элемента, дек стал {queue}')


try_add_pop_operations()

"""Задание 5: Реализация простой очереди с помощью deque.
Напишите функции для добавления и извлечения элементов из deque.
Создайте пустой deque.
Используйте написанные функции для добавления и извлечения элементов из очереди."""


# Здесь буду использовать функции, написанные выше
new_deque = deque()
add_to_end(new_deque, 'Вася')
cprint(f'Вася стал в очередь {new_deque}', c='m')
add_to_end(new_deque, 'Петя')
cprint(f'Петя стал в конец {new_deque}', c='m')
add_to_end(new_deque, 'Коля')
cprint(f'Коля стал в конец {new_deque}', c='m')
add_to_head(new_deque, 'Алиса')
cprint(f'Алиса стала в начало {new_deque}', c='m')
add_to_head(new_deque, 'Иван')
cprint(f'Иван стал в начало {new_deque}', c='m')
delite_last_element(new_deque)
cprint(f'Ушел последний человек {new_deque}', c='m')
delite_last_element(new_deque)
cprint(f'Ушел последний человек {new_deque}', c='m')
delite_first_element(new_deque)
cprint(f'Ушел первый человек {new_deque}', c='m')
