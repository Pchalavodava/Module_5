import itertools

"""Задача 1: Комбинации чисел из списка

Дан список чисел [1, 2, 3, 4]. Используя модуль itertools, 
создайте все возможные комбинации чисел длиной 2 и выведите их."""


def get_numbers_combinations_from_list(numbers_list: list[int], len_combination: int) -> None:
    """
    Функция вывода генерации и вывода на печать всех возможных комбинаций чисел из заданного
    списка длинной len_combination
    :param numbers_list: list[int]: Список чисел для обработки
    :param len_combination: int: Количество чисел в комбинации
    :return: None
    """
    for combination in itertools.combinations(numbers_list, len_combination):
        print(combination)


n_list = [1, 2, 3, 4]
get_numbers_combinations_from_list(n_list, 2)


"""Задача 2: Перебор перестановок букв в слове

Для слова 'Python' найдите все возможные перестановки букв. 
Выведите каждую перестановку на отдельной строке."""


def get_all_possible_permutations(input_word: str) -> None:
    """
    Генерация и вывод всех возможных перестановок букв в заданном слове
    :param input_word: str: Слово для обработки
    :return: None
    """
    for perm in itertools.permutations(input_word):
        print(perm)


word = 'Python'
get_all_possible_permutations(word)


"""Задача 3: Объединение списков в цикле

Даны три списка: ['a', 'b'], [1, 2, 3], ['x', 'y']. 
Используя itertools.cycle, объедините их в один список в цикле, повторяя этот цикл 5 раз."""


def merge_lists(list_to_add: list[str | int], list_2: list[str | int], list_3: list[int | str],
                repeat: int) -> None:
    """
    Функция объединения списков добавлением в первый список элементов из последующих списков.
    :param repeat: Int: Количество повторений цикла
    :param list_to_add: list[int | str]: Список, в который будут добавлены элементы
    :param list_2: list[int | str]: Список, из которого будут добавляться элементы в первый список
    :param list_3: Список, из которого будут добавляться элементы в первый список
    :return: None
    """
    count = 1
    for item in itertools.cycle(itertools.chain(list_2, list_3)):
        if count > repeat:
            break
        list_to_add.append(item)
        count += 1
    print(list_to_add)


l1 = ['a', 'b']
l2 = [1, 2, 3]
l3 = ['x', 'y']

merge_lists(l1, l2, l3, 5)


"""Задача 4: Генерация бесконечной последовательности чисел

Создайте бесконечный генератор, который будет возвращать 
последовательность чисел Фибоначчи. Выведите первые 10 чисел Фибоначчи."""


def generate_fibonacci_sequence(len_fib_list: int) -> None:
    """
    Генерация бесконечной последовательности ряда Фибоначчи
    :return: None
    """
    i, j = 0, 1
    fib_list = [i, j]
    while len(fib_list) < len_fib_list:
        lasts_elements = fib_list[-2:]
        sum_of_last_elements = list(itertools.accumulate(lasts_elements))[-1]
        fib_list.append(sum_of_last_elements)
    print(fib_list)


generate_fibonacci_sequence(10)


"""Задача 5: Составление всех возможных комбинаций слов

Используя itertools.product, создайте все возможные комбинации слов из двух списков: 
['red', 'blue'] и ['shirt', 'shoes']. Выведите каждую комбинацию на отдельной строке."""


def get_words_combinations(*args: list[str]) -> None:
    """
    Составление всех возможных комбинаций слов из заданных списков
    :param args: Подаваемые элементы для комбинации
    :return: None
    """
    tuples_list = list(itertools.product(*args))
    print(tuples_list)


list1 = ['red', 'blue']
list2 = ['shirt', 'shoes']
get_words_combinations(list1, list2)