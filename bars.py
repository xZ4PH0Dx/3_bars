import json
import sys
import os
from json.decoder import JSONDecodeError


def get_user_location():
    return [float(x) for x in input
            ('Введите долготу и широту(только'
             ' цифры и разделительные точки):\n').split()]


def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.loads(file.read())


def get_biggest_bar(bars_list):
    bar = max(
        bars_list,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount']
    )
    return bar


def get_smallest_bar(bars_list):
    bar = min(
        bars_list,
        key=lambda bar: bar['properties']['Attributes']['SeatsCount']
    )
    return bar


def get_closest_bar(bars_list, latitude, longitude):
    bar = min(
        bars_list,
        key=lambda bar: abs(
            (bar['geometry']['coordinates'][0] - latitude) -
            (bar['geometry']['coordinates'][1] - longitude)
        )
    )
    return bar


def get_bars_list(loaded_data):
    return loaded_data['features']


if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit('Вы не указали путь к файлу!')
    filepath = sys.argv[1]

    try:
        bars_list = get_bars_list(load_data(filepath))
        user_latitude, user_longitude = get_user_location()
    except (OSError, JSONDecodeError):
        sys.exit('Файл отсутствует или это не json')
    except(TypeError, ValueError):
        sys.exit('Вы ввели неверные координаты!')

    print('Самый большой бар: ',
          get_biggest_bar(bars_list)['properties']['Attributes']['Name'])

    print('Самый маленький бар: ',
          get_smallest_bar(bars_list)['properties']['Attributes']['Name'])

    print('Ближайший бар: ',
          get_closest_bar(bars_list, user_latitude, user_longitude)
          ['properties']['Attributes']['Name'])
