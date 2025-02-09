import os
import random
import shutil

"""Часть 1: Работа с файлами и директориями

Создайте программу, которая создаст новую директорию с именем "Управление_файлами".
В этой директории создайте два файла: "file1.txt" и "file2.txt".
Запишите в каждый из файлов какой-то текст.
Выведите содержимое директории на экран."""


def create_new_directory(name_of_dir: str) -> str:
    """
    Создание новой директории с заданным именем
    :param name_of_dir: str: Название новой директории
    :return: str: Абсолютный путь
    """
    current_directory: str = os.getcwd()
    new_dir: str = current_directory + '\\' + name_of_dir
    try:
        os.mkdir(new_dir)
    except FileExistsError:
        print(f'Директория "{name_of_dir}" уже существует')
    finally:
        return new_dir


def add_files_to_new_dir(direct: str, files_list: list[str]) -> list[str]:
    """
    Добавление файлов в новую директорию
    :param direct: str: Директория, куда необходимо добавить файлы
    :param files_list: list[str]: Список файлов для добавления
    :return: list[str]: Список добавленных файлов с абсолютным путем
    """
    path: str = os.path.abspath(direct)
    files_list: list[str] = list(map(lambda x: path + '\\' + x, files_list))
    for file in files_list:
        new_file = open(file, 'w', encoding='utf-8')
        new_file.close()
    return files_list


def write_to_files(some_text: str, files: list[str]) -> None:
    """
    Запись данных в файлы
    :param some_text: str: Данные для записи в файлы
    :param files: list[str]: Список файлов для записи
    :return: None
    """
    for file in files:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(some_text[random.randint(0, len(some_text)): random.randint(0, len(some_text))])


def get_directory_contents(direct: str) -> list[str]:
    """
    Получение содержимого выбранной директории
    :param direct: str: Директория для получения ее содержимого
    :return: list[str]: Содержимое выбранной директории
    """
    content: list[str] = os.listdir(direct)
    return content


def run(directory: str, files: list[str], incoming_text: str) -> None:
    """
    Программа для создания новой директории, создания в ней файлов, записи в новые файлы информации и
    вывода содержимого данной директории в консоль
    :param directory: str: Имя новой директории
    :param files: list[str]: Список файлов для создания их в новой директории
    :param incoming_text: str: Информация для записи в файлы
    :return: None
    """
    new_dir: str = create_new_directory(directory)
    new_files: list[str] = add_files_to_new_dir(new_dir, files)
    write_to_files(incoming_text, new_files)
    dir_content: list[str] = get_directory_contents(new_dir)
    print(dir_content)


file_list = ['file1.txt', 'file2.txt']
new_subdir_in_dir = 'Управление_файлами'
text = ('Часть 1: Работа с файлами и директориями. '
        'Создайте программу, которая создаст новую директорию с именем "Управление_файлами". '
        'В этой директории создайте два файла: "file1.txt" и "file2.txt". '
        'Запишите в каждый из файлов какой-то текст. Выведите содержимое директории на экран.')
run(new_subdir_in_dir, file_list, text)


"""Часть 2: Удаление файлов и директории

Удалите один из созданных файлов.
Создайте еще одну поддиректорию внутри "Управление_файлами".
Переместите оставшийся файл в эту новую поддиректорию.
Удалите исходную директорию "Управление_файлами" вместе с ее содержимым."""


def get_file_for_removing(directory: str) -> str:
    """
    Выбор файла для удаления
    :param directory: str: Директория нахождения файла
    :return: str: Случайно выбранный файл для удаления
    """
    file: str = random.choice(os.listdir(directory))
    return file


def delite_file_from_new_dir(file: str, directory: str) -> None:
    """
    Удаление выбранного файла из заданной директории
    :param file: str: Имя файла для удаления
    :param directory: str: Директория из которой необходимо удалить файл
    :return: None
    """
    path = os.path.abspath(directory + '\\' + file)
    os.remove(path)


def create_new_subdirectory(subdirectory: str, new_subdir: str) -> str:
    """
    Создание новой поддиректории в уже созданной поддиректории
    :param subdirectory: str: Созданная ранее поддиректория, в которой необходимо создать новую поддиректорию
    :param new_subdir: str: Новая поддиректория
    :return: str: Путь к новой поддиректории
    """
    subdir: str = os.path.abspath(subdirectory)
    new_subdirectory: str = subdir + '\\' + new_subdir
    try:
        os.mkdir(new_subdirectory)
    except FileExistsError:
        print(f'Директория {new_subdirectory} уже существует')
    finally:
        return new_subdirectory


def move_file(old_subdir: str, new_subdir: str) -> None:
    """
    Перемещение файлов из одной поддиректории в другую
    :param old_subdir: str: Поддиректория, из которой необходимо переместить файлы
    :param new_subdir: str: Поддиректория, куда необходимо переместить файлы
    :return: None
    """
    get_file: list[str] = os.listdir(old_subdir)
    for file in get_file:
        file_path: str = os.path.abspath(old_subdir + '\\' + file)
        if not os.path.isdir(file_path):
            new_file_path: str = new_subdir + '\\' + file
            shutil.move(file_path, new_file_path)


def del_subdir(subdir: str) -> None:
    """
    Удаление каталога
    :param subdir: str: Поддиректория, которую необходимо удалить
    :return: None
    """
    shutil.rmtree(subdir)


def run(old_subdir: str, new_subdir: str) -> None:
    """
    Программа для удаления файла из поддиректории, создание новой поддиректории в поддиректории,
    перемещения файла из старой поддиректории в новую и удаление старой поддиректории со всем ее
    содержимым
    :param old_subdir: str: Старая поддиректория
    :param new_subdir: str: Новая поддиректория
    :return: None
    """
    file_to_del: str = get_file_for_removing(old_subdir)
    delite_file_from_new_dir(file_to_del, old_subdir)
    new: str = create_new_subdirectory(old_subdir, new_subdir)
    move_file(old_subdir, new)
    del_subdir(old_subdir)


old_subdir_name = 'Управление_файлами'
new_subdir_name = 'Новая_поддиректория'
run(old_subdir_name, new_subdir_name)