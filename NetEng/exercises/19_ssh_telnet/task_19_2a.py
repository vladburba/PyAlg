# -*- coding: utf-8 -*-
"""
Задание 19.2a

Скопировать функцию send_config_commands из задания 19.2 и добавить параметр verbose,
который контролирует будет ли выводится на стандартный поток вывода
информация о том к какому устройству выполняется подключение.

verbose - это параметр функции send_config_commands, не параметр ConnectHandler!

По умолчанию, результат должен выводиться.

Пример работы функции:

In [13]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...

In [14]: result = send_config_commands(r1, commands, verbose=False)

In [15]:

Скрипт должен отправлять список команд commands на все устройства из файла devices.yaml с помощью функции
send_config_commands. """


import yaml
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException


def send_config_commands(device, commands, verbose=True):
    res = None
    if verbose:
        print('Подключаюсь к {}...'.format(device['ip']))
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            res = ssh.send_config_set(commands)
    except (NetMikoAuthenticationException, NetMikoTimeoutException) as error:
        print('Error = ', error)
    return res


if __name__ == '__main__':

    commands = [
        'logging 10.255.255.1', 'logging buffered 20010', 'no logging console'
    ]

    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for device in devices:
        result = send_config_commands(device, commands, verbose=False)
        print(result)
    print('Мы закончили свое выступление. Всем спасибо!')