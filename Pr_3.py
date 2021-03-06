#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Использовать словарь, содержащий следующие ключи: название пункта назначения рейса;
# номер рейса; тип самолета. Написать программу, выполняющую следующие действия: ввод
# с клавиатуры данных в список, состоящий из словарей заданной структуры; записи должны
# быть размещены в алфавитном порядке по названиям пунктов назначения; вывод на экран
# пунктов назначения и номеров рейсов, обслуживаемых самолетом, тип которого введен с
# клавиатуры; если таких рейсов нет, выдать на дисплей соответствующее сообщение

from datetime import date
import sys

if __name__ == '__main__':
    school = {'1a': 30, '1б': 30,
              '2а': 30, '2б': 30,
              '3а': 30, '3б': 30,
              '4а': 25, '4б': 30,
              '5а': 16, '5б': 30,
              '6а': 20, '6б': 17,
              '7а': 17, '7б': 13,
              '8а': 22, '8б': 25,
              '9a': 29, '9б': 30,
              '10a': 18, '10б': 13,
              '11a': 7, '11б': 8
              }
    print(school)

    school['5б'] += 10
    school['9в'] = 20
    school.pop('5б', 30)

    sum = 0
    for item in school.values():
        sum += item
    print(school)
    print("Количество учеников во всех классах: ", sum)
