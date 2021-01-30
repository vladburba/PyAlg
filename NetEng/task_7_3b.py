# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

new_line_list = []
with open('CAM_table.txt', 'r') as src:
    for line in src:
        # ignore_string = False
        line_list = line.split()
        # print(line)
        # print(line_list)
        try:
            first = int(line_list[0])
            # print(line_list)
            line_list[0] = first
            new_line_list.append(line_list)
            # print(new_line_list)
            # print('{:4}  {}  {:}'.format(line_list[0], line_list[1], line_list[3]))
        except(ValueError, IndexError):
            ignore_string = True
new_line_list.sort()
print(new_line_list)
vlans = int(input('Введите номер влан: '))
for line in new_line_list:
    if vlans == line[0]:
        print('{:<4}      {}      {:}'.format(line[0], line[1], line[3]))
