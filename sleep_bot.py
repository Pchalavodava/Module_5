import csv
import os
from datetime import datetime as dt

from telebot import types

import telebot

TG_TOKEN = os.getenv('TG_TOKEN')
bot = telebot.TeleBot(TG_TOKEN)
message_dict: dict[str, str] = {
    'go_to_sleep': 'Иду спать',
    'wake_up': 'Я проснулся',
    'statistic': 'Сколько я спал/а?'
}


def create_keyboard(button_name: str) -> types.ReplyKeyboardMarkup:
    """
    Конструктор для создания клавиатуры
    :param button_name: str: Название клавиши
    :return: ReplyKeyboardMarkup: Клавиатура с заданным названием клавиши
    """
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = types.KeyboardButton(button_name)
    keyboard.add(button)
    return keyboard


def write_to_csv(csv_file: str, data: list[str | int]) -> None:
    """
    Запись данных в csv-файл
    :param csv_file: str: Файл для записи
    :param data: str: Данные для записи в файл
    :return: None
    """
    with open(csv_file, 'a', encoding='utf-8') as file:
        csv.writer(file).writerow(data)


def create_list_from_csv(csv_file: str, user_id: int) -> list[list[str]]:
    """
    Чтение данных из csv-файла и создание списка операций конкретного пользователя
    :param csv_file: str: Файл, из которого необходимо сформировать список операций
    :param user_id: int: Идентификационный номер пользователя
    :return: list[list[str]]: Список операций пользователя под идентификационным номером user_id
    """
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        not_empty_lists: list[list[str]] = list(filter(lambda x: x, list(reader)))
        user_list: list[list[str]] = list(filter(lambda y: y[0] == str(user_id), not_empty_lists))
        return user_list


def press_wakeup_sleep_buttons(message: str, user_id: int, chat_id: int, file_csv: str,
                               warning_message: str, button_text: str) -> None:
    """
    Запись в файл csv списка с id пользователя, операцией пробуждения или отхода ко сну и времени операции.
    :param message: Str: Сообщение, посылаемое в бот
    :param user_id: int: Идентификатор пользователя
    :param chat_id: int: Идентификатор чата
    :param file_csv: str: Файл csv для записи
    :param warning_message: str: Сообщение, которое будет послано ботом в чат
    :param button_text: str: Название кнопки
    :return: None
    """
    time = str(dt.now())[:19]  # Здесь обрезаю миллисекунды. Не знаю, как иначе можно это сделать
    line_to_write: list[int | str] = [user_id, message, time]
    write_to_csv(file_csv, line_to_write)
    keyboard = create_keyboard(button_text)
    bot.send_message(chat_id, warning_message, reply_markup=keyboard)


def calculate_sleep_time(user_id: int, chat_id: int, file_csv: str) -> None:
    """
    Формирование двух списков, где один из них - список отхода ко сну, второй - время пробуждения.
    И дальнейший расчет разницы времени между временем пробуждения и отходом ко сну.
    :param user_id: Int: Идентификатор пользователя
    :param chat_id: int: Идентификатор чата
    :param file_csv: str: Файл для формирования из него отдельных списков
    :return: None
    """
    steps_list = create_list_from_csv(file_csv, user_id)
    try:
        my_wake_up_list = list(filter(lambda x: int(x[0]) == user_id and x[1] == message_dict['wake_up'],
                                      steps_list))[-1]
        my_go_to_sleep_list = list(filter(lambda x: int(x[0]) == user_id and x[1] == message_dict['go_to_sleep'],
                                          steps_list))[-1]
        w_time = dt.strptime(my_wake_up_list[2], "%Y-%m-%d %H:%M:%S")
        s_time = dt.strptime(my_go_to_sleep_list[2], "%Y-%m-%d %H:%M:%S")
        time_delta = (w_time - s_time).seconds
        if time_delta < 60:
            message = f'Ты спал {time_delta} секунд'
        elif 3600 > time_delta >= 60:
            minutes = time_delta // 60
            seconds = time_delta % 60
            message = f'Ты спал {minutes} минут, {seconds} секунд'
        else:
            hours = time_delta // 3600
            minutes = time_delta % 3600 // 60
            seconds = time_delta % 3600 % 60
            message = f'Ты спал {hours} часов, {minutes} минут, {seconds} секунд'
    except IndexError:
        message = 'Ты или не ложился, или уже проснулся'
    bot.send_message(chat_id, message)


@bot.message_handler(commands=['start'])
def start(message) -> None:
    """
    Обработка команды start
    :param message: Сообщение, отправляемое в чат
    :return: None
    """
    name_of_file = 'bot.csv'
    path = os.getcwd() + '\\' + name_of_file
    if not os.path.exists(path):
        open(name_of_file, 'a').close()

    list_from_csv = create_list_from_csv(name_of_file, message.from_user.id)
    if not list_from_csv or list_from_csv[-1][1] == message_dict['wake_up']:
        warning_message = 'Привет. Сообщи о своем отходе ко сну'
        keyboard = create_keyboard(message_dict['go_to_sleep'])
        bot.send_message(message.chat.id, warning_message, reply_markup=keyboard)
    else:
        warning_message = 'Не забудь предупредить, когда проснешься'
        press_wakeup_sleep_buttons(message.text, message.from_user.id, message.chat.id, 'bot.csv',
                                   warning_message, message_dict['wake_up'])


@bot.message_handler(func=lambda message: True)
def handle_message(message) -> None:
    """
    Обработка действия бота в зависимости от посланной ему команды (действия пользователя)
    :param message: Сообщение, посылаемое в бот
    :return: None
    """
    csv_file = 'bot.csv'
    if message.text == message_dict['go_to_sleep']:
        warning_message = 'Не забудь предупредить, когда проснешься'
        press_wakeup_sleep_buttons(message.text, message.from_user.id, message.chat.id, csv_file,
                                   warning_message, message_dict['wake_up'])
    if message.text == message_dict['wake_up']:
        warning_message = 'Хочешь узнать время своего сна?'
        press_wakeup_sleep_buttons(message.text, message.from_user.id, message.chat.id, csv_file,
                                   warning_message, message_dict['statistic'])
    if message.text == message_dict['statistic']:
        calculate_sleep_time(message.from_user.id, message.chat.id, csv_file)
        warning_message = 'Скажи, когда будешь ложиться спать'
        keyboard = create_keyboard(message_dict['go_to_sleep'])
        bot.send_message(message.chat.id, warning_message, reply_markup=keyboard)


bot.polling()
