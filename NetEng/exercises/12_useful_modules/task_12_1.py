# -*- coding: utf-8 -*-
'''
    Задание 12.1

    Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.

    Функция ожидает как аргумент список IP-адресов.

    Функция должна возвращать кортеж с двумя списками:
    * список доступных IP-адресов
    * список недоступных IP-адресов

    Для проверки доступности IP-адреса, используйте ping.

    Ограничение: Все задания надо выполнять используя только пройденные темы.
    '''

import subprocess

def ping_ip(ip_address):
    """
    Ping IP address and return tuple:
    On success:
        * True
        * command output (stdout)
    On failure:
        * False
        * error output (stderr)
    """
    reply = subprocess.run(['ping', '-c', '1', '-n', ip_address],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           encoding='utf-8')
    print(reply)
    if reply.returncode == 0:
        # print('result_stdout = ', reply.stdout)
        return True, reply.stdout
    else:
        # print('result_stderr = ', reply.stderr)
        return False, reply.stderr


def ping_ip_addresses(ip_addresses_list):

    good_list = []
    bad_list = []

    for ip in ip_addresses_list:

        result = ping_ip(ip)
        # print(result)

        if result[0] == True:
            good_list.append(ip)
        else:
            bad_list.append(ip)

    return good_list, bad_list


if __name__ == '__main__':
    my_ip_address_list = ['8.8.8.8', '192.168.1.1', 'a']

    print(ping_ip_addresses(my_ip_address_list))
