# -*- coding: utf-8 -*-
"""
Задание 19.2c

Скопировать функцию send_config_commands из задания 19.2b и переделать ее таким образом:

Если при выполнении команды возникла ошибка,
спросить пользователя надо ли выполнять остальные команды.

Варианты ответа [y]/n:
* y - выполнять остальные команды. Это значение по умолчанию, поэтому нажатие любой комбинации воспринимается как y
* n или no - не выполнять остальные команды

Функция send_config_commands по-прежнему должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате
* ключ - команда
* значение - вывод с выполнением команд

Проверить работу функции можно на одном устройстве.

Пример работы функции:

In [11]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...
Команда "logging 0255.255.1" выполнилась с ошибкой "Invalid input detected at '^' marker." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: y
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: n

In [12]: pprint(result)
({},
 {'logging': 'config term\n'
             'Enter configuration commands, one per line.  End with CNTL/Z.\n'
             'R1(config)#logging\n'
             '% Incomplete command.\n'
             '\n'
             'R1(config)#',
  'logging 0255.255.1': 'config term\n'
                        'Enter configuration commands, one per line.  End with '
                        'CNTL/Z.\n'
                        'R1(config)#logging 0255.255.1\n'
                        '                   ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'R1(config)#'})

"""


import yaml
from pprint import pprint
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException


def send_config_commands(dev, com_list, verbose=True):
    error_list = ['Invalid input detected', 'Incomplete command', 'Ambiguous command']
    good_list = {}
    bad_list = {}
    output = {}
    if verbose:
        print('Подключаюсь к {} config commands = {}...'.format(dev['ip'], com_list))
    try:
        with ConnectHandler(**dev) as ssh:
            ssh.enable()
            for command in com_list:
                output[command] = ssh.send_config_set(command)

                if error_list[0] in output[command]:
                    print("""Команда "{}" выполнилась с ошибкой "{}" на устройстве {}""".format(command, error_list[0],
                                                                                                dev['ip']))
                    bad_list[command] = output[command]
                    choice = input('Продолжать выполнять команды? [y]/n: y ')
                    if choice == 'n':
                        return good_list, bad_list
                elif error_list[1] in output[command]:
                    print("""Команда "{}" выполнилась с ошибкой "{}" на устройстве {}""".format(command, error_list[1],
                                                                                                dev['ip']))
                    bad_list[command] = output[command]
                    choice = input('Продолжать выполнять команды? [y]/n: y ')
                    if choice == 'n':
                        return good_list, bad_list
                elif error_list[2] in output[command]:
                    print("""Команда "{}" выполнилась с ошибкой "{}" на устройстве {}""".format(command, error_list[2],
                                                                                                dev['ip']))
                    bad_list[command] = output[command]
                    choice = input('Продолжать выполнять команды? [y]/n: y ')
                    if choice == 'n':
                        return good_list, bad_list
                else:
                    print("""Команда "{}" выполнилась без ошибок на устройстве {}""".format(command, dev['ip']))
                    good_list[command] = output[command]
    except (NetMikoAuthenticationException, NetMikoTimeoutException, SSHException) as error:
        print('Error = ', error)

    return good_list, bad_list


if __name__ == '__main__':

    commands_with_errors = ['logging 0255.255.1', 'logging', 'a']
    correct_commands = ['logging buffered 20010', 'ip http server']
    commands = correct_commands + commands_with_errors
    result = {}
    all_result = {}

    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for device in devices:
        result = send_config_commands(device, commands)
        all_result[device['ip']] = result
    pprint(all_result, width=120)
    print('Мы закончили свое выступление. Всем спасибо!')
