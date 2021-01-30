# -*- coding: utf-8 -*-
"""
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

"""


def parse_sh_ip_int_br(file='sh_ip_int_br.txt'):
    import re
    from pprint import pprint
    interface_list = []

    with open(file, 'r') as f:
        for line in f:
            # print(line.rstrip())
            match = re.search(r'(\S+) + (\d+.\d+.\d+.\d+|unassigned) +(\S+) +(\S+) +(\S+) +(\S+)', line)
            if match:
                # print('match = ', match.groups())
                if match.group(5) == 'administratively':
                    # print(match.groups())
                    interface_list.append((match.group(1), match.group(2), 'administratively down', match.group(6)))
                else:
                    interface_list.append((match.group(1), match.group(2), match.group(5), match.group(6)))

    # pprint(interface_list)

    return interface_list


if __name__ == '__main__':
    print(parse_sh_ip_int_br())
