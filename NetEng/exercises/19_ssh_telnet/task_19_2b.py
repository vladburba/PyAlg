# -*- coding: utf-8 -*-
"""
Задание 19.2b

Скопировать функцию send_config_commands из задания 19.2a и добавить проверку на ошибки.

При выполнении каждой команды, скрипт должен проверять результат на такие ошибки:
 * Invalid input detected, Incomplete command, Ambiguous command

Если при выполнении какой-то из команд возникла ошибка,
функция должна выводить сообщение на стандартный поток вывода с информацией
о том, какая ошибка возникла, при выполнении какой команды и на каком устройстве, например:
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1

Ошибки должны выводиться всегда, независимо от значения параметра verbose.
При этом, verbose по-прежнему должен контролировать будет ли выводиться сообщение:
Подключаюсь к 192.168.100.1...


Функция send_config_commands теперь должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате:
* ключ - команда
* значение - вывод с выполнением команд

Проверить работу функции можно на одном устройстве.


Пример работы функции send_config_commands:

In [16]: commands
Out[16]:
['logging 0255.255.1',
 'logging',
 'a',
 'logging buffered 20010',
 'ip http server']

In [17]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...
Команда "logging 0255.255.1" выполнилась с ошибкой "Invalid input detected at '^' marker." на устройстве 192.168.100.1
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1
Команда "a" выполнилась с ошибкой "Ambiguous command:  "a"" на устройстве 192.168.100.1

In [18]: pprint(result, width=120)
({'ip http server': 'config term\n'
                    'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                    'R1(config)#ip http server\n'
                    'R1(config)#',
  'logging buffered 20010': 'config term\n'
                            'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                            'R1(config)#logging buffered 20010\n'
                            'R1(config)#'},
 {'a': 'config term\n'
       'Enter configuration commands, one per line.  End with CNTL/Z.\n'
       'R1(config)#a\n'
       '% Ambiguous command:  "a"\n'
       'R1(config)#',
  'logging': 'config term\n'
             'Enter configuration commands, one per line.  End with CNTL/Z.\n'
             'R1(config)#logging\n'
             '% Incomplete command.\n'
             '\n'
             'R1(config)#',
  'logging 0255.255.1': 'config term\n'
                        'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                        'R1(config)#logging 0255.255.1\n'
                        '                   ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'R1(config)#'})

In [19]: good, bad = result

In [20]: good.keys()
Out[20]: dict_keys(['logging buffered 20010', 'ip http server'])

In [21]: bad.keys()
Out[21]: dict_keys(['logging 0255.255.1', 'logging', 'a'])


Примеры команд с ошибками:
R1(config)#logging 0255.255.1
                   ^
% Invalid input detected at '^' marker.

R1(config)#logging
% Incomplete command.

R1(config)#a
% Ambiguous command:  "a"
"""


import yaml
from pprint import pprint
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException


def send_config_commands(dev, com_list, verbose=True):
    error_list = ['Invalid input detected', 'Incomplete command', 'Ambiguous command']
    good_list = {}
    bad_list = {}
    output = {}
    if verbose:
        print('Подключаюсь к {}...'.format(dev['ip']))
    try:
        with ConnectHandler(**dev) as ssh:
            ssh.enable()
            for command in com_list:
                output[command] = ssh.send_config_set(command)

                if error_list[0] in output[command]:
                    print("""Команда "{}" выполнилась с ошибкой "{}" на устройстве {}""".format(command, error_list[0],
                                                                                                dev['ip']))
                    bad_list[command] = output[command]
                elif error_list[1] in output[command]:
                    print("""Команда "{}" выполнилась с ошибкой "{}" на устройстве {}""".format(command, error_list[1],
                                                                                                dev['ip']))
                    bad_list[command] = output[command]
                elif error_list[2] in output[command]:
                    print("""Команда "{}" выполнилась с ошибкой "{}" на устройстве {}""".format(command, error_list[2],
                                                                                                dev['ip']))
                    bad_list[command] = output[command]
                else:
                    print("""Команда "{}" выполнилась без ошибок на устройстве {}""".format(command, dev['ip']))
                    good_list[command] = output[command]
    except (NetMikoAuthenticationException, NetMikoTimeoutException) as error:
        print('Error = ', error)
    good_bad = (good_list, bad_list)
    return good_bad


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
