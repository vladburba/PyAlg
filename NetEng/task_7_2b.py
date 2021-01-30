# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

with open(argv[1], 'r') as src, open('config_sw1_cleared.txt', 'w') as dest:
    for line in src:

        ignore_string = False

        for word in ignore:

            if word in line:
                ignore_string = True
                # print('Слово = ', word)
                # print('Строка = ', line.rstrip())
                break
        if not ignore_string:
            # print(line.rstrip())
            dest.write(line)




