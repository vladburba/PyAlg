# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""


def get_ints_without_description(file_name):
    import re
    int_list = []
    with open(file_name, 'r') as f:
        for line in f:
            # print(line.rstrip())
            match = re.match(r'interface (?P<intf>\S+)', line)
            if match:
                interface = match.group('intf')
                # print(match)
                # print('int = ', interface)
                int_list.append(interface)
            elif re.match(r' description', line):
                int_list.pop()

    return int_list


if __name__ == '__main__':
    print(sorted(get_ints_without_description('config_r1.txt')))
