#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json
import sys
import os


filepath = str(sys.argv[1])
user_choices = ['1', '2', '3', 1, 2, 3]
user_choice = None
user_latitude = None
user_longitude = None


def ask_user_location():
    return [float(x) for x in input
            ('Введите долготу и широту(только'
             ' цифры и разделительные точки): ').split()]


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file:
        return json.loads(file.read())


def get_biggest_bar(bars_list):
    processed_data = max(bars_list, key=lambda bar: bar['properties']
                                                       ['Attributes']
                                                       ['SeatsCount'])
    return processed_data['properties']['Attributes']['Name']


def get_smallest_bar(bars_list):
    processed_data = min(bars_list, key=lambda bar: bar['properties']
                                                       ['Attributes']
                                                       ['SeatsCount'])
    return processed_data['properties']['Attributes']['Name']


def get_closest_bar(bars_list, latitude, longitude):
    processed_data = min(
        bars_list,
        key=lambda bar: abs(
            (bar['geometry']['coordinates'][0] - latitude) -
            (bar['geometry']['coordinates'][1] - longitude)
        )
    )
    return processed_data['properties']['Attributes']['Name']


def print_choices():
    return input('Что Вы хотите найти?\n'
                 '  1) Самый большой бар\n'
                 '  2) Самый маленький бар\n'
                 '  3) Ближайший бар\n')


def get_bars_list(loaded_data):
    return loaded_data['features']


if __name__ == '__main__':

    while user_choice not in user_choices:
        user_choice = print_choices()

    bars_list = get_bars_list(load_data(filepath))
    if not bars_list:
        print('Проверьте корректность пути')

    if int(user_choice) == 1:
        print('Самый большой бар: ',
              str(get_biggest_bar(bars_list)))

    elif int(user_choice) == 2:
        print('Самый маленький бар: ',
              str(get_smallest_bar(bars_list)))

    elif int(user_choice) == 3:
        try:
            user_latitude, user_longitude = ask_user_location()
        except (ValueError, TypeError):
            user_latitude, user_longitude = ask_user_location()
        print('Ближайший бар: ',
              str(get_closest_bar(bars_list, user_latitude, user_longitude)))
