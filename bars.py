#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json
import sys


def ask_user_location():
    return [float(x) for x in input
                ('Введите долготу и широту(только'
                 ' цифры и разделительные точки): ').split()]


def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.loads(file.read())


def get_biggest_bar(bars_list):
    return max(bars_list, key=lambda bar: bar['properties']
               ['Attributes']['SeatsCount'])


def get_smallest_bar(bars_list):
    return min(bars_list, key=lambda bar: bar['properties']
               ['Attributes']['SeatsCount'])


def get_closest_bar(bars_list, latitude, longitude):
    return min(
        bars_list,
        key=lambda bar: abs(
            (bar['geometry']['coordinates'][0] - latitude) -
            (bar['geometry']['coordinates'][1] - longitude)
        )
    )


def print_choices():
    return int(input('''Что Вы хотите найти?
          1) Самый большой бар
          2) Самый маленький бар
          3) Ближайший бар'''))


def get_bars_list(bars):
    return bars['features']


if __name__ == '__main__':
    filepath = str(sys.argv[1])

    try:
        user_choice = print_choices()
    except ValueError:
        print('Нет такого варианта')
        user_choice = print_choices()

    try: 
        bars = load_data(filepath)
    except(FileNotFoundError):
        print('Файл не найден или поврежден')

    bars_list = get_bars_list(bars)

    if user_choice == 1:
        print('Самый большой бар: ',
              str(get_biggest_bar(bars_list)))

    elif user_choice == 2:
        print('Самый маленький бар: ',
              str(get_smallest_bar(bars_list)))

    elif user_choice == 3:
        try:
            user_latitude, user_longitude = ask_user_location()
        except (ValueError, TypeError):
            print('Неправильно введены данные')
            #exit()
        
        print('Ближайший бар: ',
              str(get_closest_bar(bars_list, user_latitude, user_longitude)))
