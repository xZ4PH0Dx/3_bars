import json


def ask_file_path():
    return input('Введите путь, по которому лежат файлы:\n')


def ask_user_location():
    try:
        return [float(x) for x in input
                ('Введите долготу и широту(только'
                 ' цифры и разделительные точки): ')
                .split()]
    except (ValueError, TypeError):
        print('Неправильно введены данные')


def load_json(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.loads(file.read())
    except FileNotFoundError:
        print('Файл отсутствует!')


def get_biggest_bar(bars_list):
    return max(bars_list, key=lambda bar: bar['properties']
                                             ['Attributes']
                                             ['SeatsCount'])


def get_smallest_bar(bars_list):
    return min(bars_list, key=lambda bar: bar['properties']
                                             ['Attributes']
                                             ['SeatsCount'])


def get_closest_bar(bars_list, longitude, latitude):
    return min(bars_list, key=lambda bar:
               abs(abs(bar['geometry']['coordinates'][0] - longitude) -
                   abs(bar['geometry']['coordinates'][1] - latitude)))


def print_choices():
    return int(input('''Что Вы хотите найти?
    1) Самый большой бар
    2) Самый маленький бар
    3) Ближайший бар
    0) Выйти из программы\n
    '''))

def get_bars_list():
    return load_json(ask_file_path())['features']


if __name__ == '__main__':
    user_choice = print_choices()

    if user_choice == 1:
        print('Самый большой бар: ',
              str(get_biggest_bar(get_bars_list()))
              .replace('{', '').replace('}', ''))

    elif user_choice == 2:
        print('Самый маленький бар: ',
              str(get_smallest_bar(get_bars_list()))
              .replace('{', '').replace('}', ''))

    elif user_choice == 3:
        user_longitude, user_latitude = ask_user_location()
        get_closest_bar(get_bars_list(), user_longitude, user_latitude)

    elif user_choice == 0:
        exit()
