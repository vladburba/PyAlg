# -*- coding: utf-8 -*-
"""
Задание 19.3

Создать функцию send_commands (для подключения по SSH используется netmiko).

Параметры функции:
* device - словарь с параметрами подключения к устройству, которому надо передать команды
* show - одна команда show (строка)
* config - список с командами, которые надо выполнить в конфигурационном режиме

В зависимости от того, какой аргумент был передан, функция вызывает разные функции внутри.
При вызове функции send_commands, всегда будет передаваться только один из аргументов show, config.

Далее комбинация из аргумента и соответствующей функции:
* show - функция send_show_command из задания 19.1
* config - функция send_config_commands из задания 19.2

Функция возвращает строку с результатами выполнения команд или команды.

Проверить работу функции:
* со списком команд commands
* командой command

Пример работы функции:

In [14]: send_commands(r1, show='sh clock')
Out[14]: '*17:06:12.278 UTC Wed Mar 13 2019'

In [15]: send_commands(r1, config=['username user5 password pass5', 'username user6 password pass6']) Out[15]:
'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#username user5 password
pass5\nR1(config)#username user6 password pass6\nR1(config)#end\nR1#' """

from ssh_show_command import send_show_command
from ssh_config_commands import send_config_commands
import yaml


# from pprint import pprint


def send_commands(device, **kwargs):
    show_com = kwargs.get('show')
    conf_list = kwargs.get('config')
    if show_com:
        string = send_show_command(device, show_com)
        return string
    elif conf_list:
        string = send_config_commands(device, conf_list, verbose=True)
        return string


if __name__ == "__main__":
    commands = ['logging 10.255.255.1', 'logging buffered 20010', 'no logging console']
    command = 'sh run'
    result = {}
    all_result = {}

    with open("dc_dev_list.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        result_show = send_commands(dev, show=command)
        file_name = dev['ip'] + '_run.cfg'
        if result_show:
            with open(file_name, 'w') as f:
                # print(result_show)
                f.write(result_show)

        # all_result[dev['ip'] + '_show'] = result_show
        # pprint(result_show, width=120)
        # result_conf = send_commands(dev, config=commands)
        # all_result[dev['ip'] + '_conf'] = result_conf
        # pprint(result_conf, width=120)

    # pprint(all_result, width=120)
    print('Мы закончили свое выступление. Всем спасибо!')
