"""
1. Дан список строк ["apple", "kiwi", "banana", "fig"]. Оставьте в нем только строки,
длина которых больше 4 символов, используя filter() и лямбда-функцию.

"""


def select_by_length(input_list: list[str]) -> list[str]:
    """
    Отбор элементов списка по условию, что количество символов в строке больше четырех
    :param input_list: list[str]: Входящий список для фильтрации
    :return: list[str]: Список, где строки превышают четыре символа
    """
    more_than_four_list: list[str] = list(filter(lambda x: len(x) > 4, input_list))
    return more_than_four_list


fruit_list: list[str] = ["apple", "kiwi", "banana", "fig"]
print(select_by_length(fruit_list))

"""
2. Дан список словарей students = [{"name": "John", "grade": 90}, {"name": "Jane", "grade": 85}, {"name": "Dave", "grade": 92}].
Найдите студента с максимальной оценкой, используя max() и лямбда-функцию для задания ключа сортировки.

"""


def select_max_grade_student(students_list: list[dict[str, int]]) -> dict[str, int]:
    """
    Поиск студента с наивысшим баллом
    :param students_list: list[dict[str, int]]: Список словарей (студентов), где ключами являются имя студента
    и его оценка
    :return: dict[str, int]: Словарь (студент с наивысшим баллом) с максимальным значением ключа 'grade'.
    """
    max_grade_student: dict[str, int] = max(students_list, key=lambda student: student['grade'])
    return max_grade_student


students: list[dict[str, int]] = [
    {"name": "John", "grade": 90},
    {"name": "Jane", "grade": 85},
    {"name": "Dave", "grade": 92}
]
print(select_max_grade_student(students))

"""
3.  Дан список кортежей [(1, 5), (3, 2), (2, 8), (4, 3)].
Отсортируйте его по сумме элементов каждого кортежа с использованием sorted() и лямбда-функции.

"""


def sort_tuples(list_to_sort: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Функция сортировки списка кортежей по сумме элементов каждого из кортежей
    :param list_to_sort: List[tuple[int, int]: Входящий список кортежей для сортировки
    :return: list[tuple[int, int]]: Отсортированный список кортежей по сумме элементов
    """
    sorted_tuple_list: list[tuple[int, int]] = sorted(list_to_sort, key=lambda x: x[0] + x[1])
    return sorted_tuple_list


tuple_list: list[tuple[int, int]] = [(1, 5), (3, 2), (2, 8), (4, 3)]
print(sort_tuples(tuple_list))

"""
4. Дан список чисел [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
Оставьте в нем только четные числа с использованием filter() и лямбда-функции.

"""


def get_list_even_numbers(input_list: list[int]) -> list[int]:
    """
    Получение списка четных чисел из заданного списка
    :param input_list: list[int]: Список для отбора четных чисел
    :return: list[int]: Список четных чисел
    """
    even_numbers: list[int] = list(filter(lambda x: x % 2 == 0, input_list))
    return even_numbers


num_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_list_even_numbers(num_list))

"""
5. Сортировка объектов пользовательского класса:
Создайте класс Person с атрибутами name и age. Дан список объектов этого класса.
Отсортируйте список объектов по возрасту с использованием sorted() и лямбда-функции.

"""


class Person:
    """
    Класс - человек с атрибутами имя и возраст (name, age)
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Конструктор создания объекта человек
        :param name: str: Имя
        :param age: int: Возраст
        """
        self.name = name
        self.age = age

    def __repr__(self):
        """
        Строковое представление объекта Человек
        :return: str: Имя и возраст
        """
        return f'{self.name} - {self.age}'


def sort_from_younger_to_older(peoples_list: list[Person]) -> list[Person]:
    """
    Сортировка списка людей по возрасту, по возрастанию
    :param peoples_list: list[People]: Список объектов класса People с именем и возрастом
    :return: list[People]: Отсортированный список объектов класса People по возрастанию возраста
    """
    sorted_age_people = sorted(peoples_list, key=lambda human: human.age)
    return sorted_age_people


people = [
    Person('Vladislav', 30),
    Person('Gabriella', 28),
    Person('Anastasie', 31),
    Person('Jaroslav', 21)
]

print(sort_from_younger_to_older(people))