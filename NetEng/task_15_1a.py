# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

"""


def get_ip_from_cfg(file='config_r1.txt'):
    import re
    interface_dict = {}

    with open(file, 'r') as f:
        for line in f:
            if line.startswith('interface'):
                interface = re.search(r'interface (\S+)', line).group(1)
                interface_dict[interface] = {}
            elif re.search(r'ip address (\S+) (\S+)', line):
                ip = re.search(r'ip address (\S+) (\S+)', line).group(1)
                mask = re.search(r'ip address (\S+) (\S+)', line).group(2)
                ip_adr = (ip, mask)
                interface_dict[interface] = ip_adr
                # print(interface_dict)

        result = interface_dict.copy()
        for interface in result:
            if result[interface] == {}:
                del interface_dict[interface]

    return interface_dict


if __name__ == '__main__':
    print(get_ip_from_cfg())
