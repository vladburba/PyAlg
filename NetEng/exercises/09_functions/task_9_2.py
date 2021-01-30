# -*- coding: utf-8 -*-
'''
Задание 9.2

Создать функцию generate_trunk_config, которая генерирует конфигурацию для trunk-портов.

У функции должны быть такие параметры:

- intf_vlan_mapping: ожидает как аргумент словарь с соответствием интерфейс-VLANы такого вида:
    {'FastEthernet0/1': [10, 20],
     'FastEthernet0/2': [11, 30],
     'FastEthernet0/4': [17]}
- trunk_template: ожидает как аргумент шаблон конфигурации trunk-портов в виде списка команд (список trunk_mode_template)

Функция должна возвращать список команд с конфигурацией
на основе указанных портов и шаблона trunk_mode_template.
В конце строк в списке не должно быть символа перевода строки.

Проверить работу функции на примере словаря trunk_config.

Пример итогового списка (перевод строки после каждого элемента сделан для удобства чтения):
[
'interface FastEthernet0/1',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan 10,20,30',
'interface FastEthernet0/2',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan 11,30',
...]


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}


def generate_trunk_config(intf_vlan_mapping, trunk_template):
    trunk_mode_list = []
    for mode, vlans in intf_vlan_mapping.items():
        trunk_mode_list.append('interface {}'.format(mode))
        # print(trunk_mode_list)
        # print(vlans)
        vlan_str = str(vlans).lstrip('[').rstrip(']').replace(' ', '')
        # print(vlan_str)

        for command in trunk_template:
            if 'allowed vlan' in command:
                trunk_mode_list.append('{} {}'.format(command, vlan_str))
            else:
                trunk_mode_list.append(command)
    return trunk_mode_list


print(generate_trunk_config(intf_vlan_mapping=trunk_config, trunk_template=trunk_mode_template))
