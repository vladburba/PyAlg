# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.


Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""

ip_ranges_list = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']


def convert_ranges_to_ip_list(ip_ranges):
    print(ip_ranges)
    ip_list = []

    for address in ip_ranges:
        # print(ip_addr)
        if '-' in address:
            address_list = address.split('-')
            # print('address = ', address)
            # print('address_list = ', address_list)

            if '.' not in address_list[1]:
                print('short_range = ', address_list)
                last_ip_num = int(address_list[1])
                first_ip_num_list = address_list[0].split('.')
                # print('fisrt_ip_num_list = ', first_ip_num_list)
                first_ip_num = int(first_ip_num_list[3])
                print('first_ip_num =', first_ip_num)
                print('last_ip_num = ', last_ip_num)
                for _ in range(first_ip_num, last_ip_num + 1):
                    # print('first_ip_num_list  = ', first_ip_num_list[:3])
                    ip_addr = '.'.join(first_ip_num_list[:3]) + '.' + str(_)
                    ip_list.append(ip_addr)
                    print('ip_list = ', ip_list)

            else:
                print('long_range = ', address_list)
                first_ip_num_list = address_list[0].split('.')
                first_ip_num = int(first_ip_num_list[3])
                print('first_ip_num =', first_ip_num)
                last_ip_num_list = address_list[1].split('.')
                last_ip_num = int(last_ip_num_list[3])
                print('last_ip_num = ', last_ip_num)
                for _ in range(first_ip_num, last_ip_num + 1):
                    # print('first_ip_num_list  = ', first_ip_num_list[:3])
                    ip_addr = '.'.join(first_ip_num_list[:3]) + '.' + str(_)
                    ip_list.append(ip_addr)
                    print('ip_list = ', ip_list)

        else:
            ip_list.append(address)
            print('ip_list = ', ip_list)

    return ip_list


if __name__ == '__main__':
    print('ip_list = ', convert_ranges_to_ip_list(ip_ranges_list))
