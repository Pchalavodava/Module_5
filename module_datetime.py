"""
Часть 1: Работа с текущей датой и временем

Получите текущую дату и время.
Выведите на экран день недели для этой даты.
Определите, является ли год текущей даты високосным, и выведите соответствующее сообщение."""
import datetime as dt


def get_currant_date() -> dt.datetime:
    """
    Получение текущей даты и времени
    :return: datetime: Текущие дата и время
    """
    return dt.datetime.now()


def get_week_day(date: dt.datetime) -> str:
    """
    Получение строкового представления дня недели
    :param date: datetime: Дата и время для определения дня недели
    :return: str: Название дня недели из полученной даты
    """
    week: list[str] = ['Понедельник',
                       'Вторник',
                       'Среда',
                       'Четверг',
                       'Пятница',
                       'Суббота',
                       'Воскресенье']
    number_of_week_day: int = date.weekday()
    week_day: str = week[number_of_week_day]
    return week_day


def is_year_leap(date: dt.datetime) -> bool:
    """
    Поверка является ли выбранный год високосным
    :param date: datetime: Дата для проверки на то, является
    :return:
    """
    year: int = date.year
    return int(year) % 400 == 0 or (int(year) % 4 == 0 and int(year) % 100 != 0)


def output_of_result_checking_of_the_current_date() -> None:
    """
    Вывод информации о текущей дате с получением названия дня недели и проверки, является ли год високосным
    :return: None
    """
    currant_date: dt.datetime = get_currant_date()
    week_day: str = get_week_day(currant_date)
    leap_year: bool = is_year_leap(currant_date)
    print(f'Текущая дата {currant_date}\n'
          f'Сегодня {week_day}\n'
          f'Является ли нынешний год високосным? {'Да' if leap_year else 'Нет'}')


output_of_result_checking_of_the_current_date()

"""Часть 2: Работа с пользовательской датой

Запросите у пользователя ввод даты в формате "год-месяц-день" (например, "2023-12-31").
Определите, сколько дней осталось до введенной даты от текущей даты.
Рассчитайте разницу между этими двумя датами и выведите результат в формате дней, часов и минут.
"""


def create_date(date: str) -> dt.datetime:
    """
    Формирование объекта datetime из строки
    :param date: str: Текстовое представление даты, введенной пользователем
    :return: datetime: Объект datetime
    """
    date_string = dt.datetime.strptime(date, '%Y-%m-%d')
    return date_string


def calculation_days_difference(date: dt.datetime) -> tuple[int, int, int]:
    """
    Расчет разницы в днях, часах и минутах
    :param date: dt.datetime: введенная и преобразованная, в объект datetime, пользователем дата
    :return: tuple[int, int, int]: Кортеж из количества дней, часов и минут
    """
    current_date: dt.datetime = dt.datetime.now()

    if current_date > date:
        difference: tuple[int, int, int] = current_date - date
    else:
        difference: tuple[int, int, int] = date - current_date
    days_difference: int = difference.days
    times_difference_hours: int = difference.seconds // 3600
    times_difference_minutes: int = difference.seconds // 60 - times_difference_hours * 60
    return days_difference, times_difference_hours, times_difference_minutes


def output_of_calculation_difference_date() -> None:
    """
    Вывод результата вычислений разницы в датах
    :return: None
    """
    user_date: str = input('Введите дату в формате ГГГГ-ММ-ДД >>> ').strip()
    try:
        date: dt.datetime = create_date(user_date)
        dates_difference: tuple[int, int, int] = calculation_days_difference(date)
        print(f'Введенная пользователем дата - {date}\n'
              f'Разница между датой пользователя и нынешней датой - {dates_difference[0]} дней, '
              f'{dates_difference[1]} часов и {dates_difference[2]} минут')
    except (ValueError, IndexError):
        print('Неверные формат даты')


output_of_calculation_difference_date()
