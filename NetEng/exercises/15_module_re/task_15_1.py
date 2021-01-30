# -*- coding: utf-8 -*-
"""
Задание 15.1

Создать функцию get_ip_from_cfg, которая ожидает как аргумент имя файла,
в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать IP-адреса и маски,
которые настроены на интерфейсах, в виде списка кортежей:
* первый элемент кортежа - IP-адрес
* второй элемент кортежа - маска

Например (взяты произвольные адреса):
[('10.0.1.1', '255.255.255.0'), ('10.0.2.1', '255.255.255.0')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.


Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

"""


def get_ip_from_cfg(file='config_r1.txt'):
    import re
    ip_adr_list = []
    regex = r'ip address (\S+) (\S+)'

    with open(file, 'r') as f:
        for line in f:
            print(line.strip('\n'))
            match = re.search(regex, line)
            # print(match)
            if match:
                ip = match.group(1)
                mask = match.group(2)
                # print('ip , mask = ', ip, mask)
                ip_adr = (ip, mask)
                # print(ip_adr)
                ip_adr_list.append(ip_adr)
                # print(ip_adr_list)

    return ip_adr_list


if __name__ == '__main__':
    print(get_ip_from_cfg())
