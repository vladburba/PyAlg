# -*- coding: utf-8 -*-
'''
Задание 7.3

Скрипт должен обрабатывать записи в файле CAM_table.txt.
Каждая строка, где есть MAC-адрес, должна быть обработана таким образом,
 чтобы на стандартный поток вывода была выведена таблица вида (показаны не все строки из файла):

 100    01bb.c580.7000   Gi0/1
 200    0a4b.c380.7000   Gi0/2
 300    a2ab.c5a0.7000   Gi0/3
 100    0a1b.1c80.7000   Gi0/4
 500    02b1.3c80.7000   Gi0/5
 200    1a4b.c580.7000   Gi0/6
 300    0a1b.5c80.7000   Gi0/7

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
# god_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# print(god_char)

with open('CAM_table.txt', 'r') as src:
    for line in src:
        # ignore_string = False
        line_list = line.split()
        # print(line)
        # print(line_list)
        try:
            int(line_list[0])
            # print(line_list[0], line_list[1], line_list[3])
            print('{:4}  {}  {:}'.format(line_list[0], line_list[1], line_list[3]))
        except(ValueError, IndexError):
            ignore_string = True
        # else:
        #     if not ignore_string:
        #          print(line_list[0], line_list[1], line_list[3])

        # for word in god_char:
        #     pass

        # if not ignore_string:
        #     print(line.rstrip())
