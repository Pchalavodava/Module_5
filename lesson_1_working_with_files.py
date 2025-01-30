import string


def get_words(file: str) -> list[str]:
    """
    Чтение текстового документа с формированием из него списка слов для дальнейшей обработки
    :param file: str: Файл для обработки
    :return: list[str]: Список слов из выбранного файла
    """
    words_list = []
    with open(file, mode='r', encoding='utf-8') as f:
        for line in f:
            s = line.translate(str.maketrans('', '', string.punctuation))
            for word in s.split():
                words_list.append(word.lower())
        return words_list


def get_words_dict(words: list[str]) -> dict[str, int]:
    """
    Создание словаря "слово: количество повторений" из выбранного файла
    :param words: list[str]: Используемый файл
    :return: dict[str, int]: Словарь, где ключ - уникальное слово, значение = количество его повторений
    """
    words_dict = {}
    for word in words:
    #     if word not in words_dict:
    #         words_dict[word] = 1
    #     else:
    #         words_dict[word] += 1
        words_dict[word] = words_dict.get(word, 0) + 1
    return words_dict


def print_words_statistic() -> None:
    """
    Функция вывода на печать статистических данных по выбранному файлу
    :return: None: Так как выводит на печать
    """
    file = input('Введите название файла: >>>').strip()
    if not file.endswith('.txt'):
        file += '.txt'
    try:
        words_list = get_words(file)
        words_dict = get_words_dict(words_list)
        print(f'Количество слов: {len(words_list)}\n'
              f'Количество уникальных слов: {len(words_dict)}\n'
              f'Все использованные слова:')
        for key, value in words_dict.items():
            print(f'{key}: {value}')
    except Exception as exc:
        print(exc)


print_words_statistic()
