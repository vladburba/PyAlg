# -*- coding: utf-8 -*-
"""
Задание 19.1b

Скопировать функцию send_show_command из задания 19.1a и переделать ее таким образом,
чтобы обрабатывалось не только исключение, которое генерируется
при ошибке аутентификации на устройстве, но и исключение,
которое генерируется, когда IP-адрес устройства недоступен.

При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.

Для проверки измените IP-адрес на устройстве или в файле devices.yaml.
"""

import yaml
from paramiko.ssh_exception import SSHException
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException


def send_show_command(device, command, verbose=True):
    if verbose:
        print('Подключаюсь к {} show command = {}...'.format(device['ip'], command))
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
        return result
    except (NetMikoAuthenticationException, NetMikoTimeoutException) as error:
        print('Error = ', error)
    except SSHException as error:
        print('Error = ', error)


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        res = send_show_command(dev, "sh ip int br")
        print(res)
