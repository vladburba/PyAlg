# -*- coding: utf-8 -*-
"""
Задание 15.1b

Проверить работу функции get_ip_from_cfg из задания 15.1a на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким образом,
чтобы в значении словаря она возвращала список кортежей для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.
Ключом остается имя интерфейса.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

"""


def get_ip_from_cfg(file='config_r2.txt'):
    import re
    from pprint import pprint
    interface_dict = {}

    with open(file, 'r') as f:
        for line in f:
            # print(line.rstrip())
            if line.startswith('interface'):
                ip_adr_list = []
                interface = re.search(r'interface (\S+)', line).group(1)
                interface_dict[interface] = {}
            elif re.search(r'ip address (\S+) (\S+)', line):
                ip = re.search(r'ip address (\S+) (\S+)', line).group(1)
                mask = re.search(r'ip address (\S+) (\S+)', line).group(2)
                ip_adr = (ip, mask)
                ip_adr_list.append(ip_adr)
                # print('ip addr = ', ip_adr)
                interface_dict[interface] = ip_adr_list
                # print('ip adr list = ', ip_adr_list)
                # print(interface_dict)

        result = interface_dict.copy()
        # print(result)
        for interface in result:
            if result[interface] == {}:
                del interface_dict[interface]

    return interface_dict


if __name__ == '__main__':
    print(get_ip_from_cfg())
