# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(config_filename = 'config_sw1.txt'):
    ports_tuple = tuple()
    access_dict = {}
    trunk_dict = {}
    with open(config_filename, 'r') as f:
        for line in f:
            # print(line.rstrip())
            if 'interface' in line:
                key = line.rstrip().replace('interface ', '')
                # print(key)
            elif 'allowed vlan' in line:
                # print(line)
                vlan_str_list = line.replace(' switchport trunk allowed vlan ', '').rstrip().split(',')
                # print(vlan_str_list)
                vlan_list = []
                for _ in vlan_str_list:
                    vlan_list.append(int(_))

                # print(vlan_list)
                trunk_dict[key] = vlan_list
            elif ('switchport mode access' in line):
                access_dict[key] = 1
            elif 'switchport access vlan' in line:
                access_dict[key] = int((line.replace(' switchport access vlan ', '').rstrip()))


    ports_tuple = (access_dict,trunk_dict)
    return ports_tuple


print(get_int_vlan_map())








# def get_int_vlan_map(config_filename = 'config_sw1.txt'):
#     ports_tuple = tuple()
#     access_dict = {}
#     trunk_dict = {}
#     with open(config_filename, 'r') as f:
#         for line in f:
#             # print(line.rstrip())
#             if 'interface' in line:
#                 key = line.rstrip()
#             elif 'allowed vlan' in line:
#                 print(line)
#                 trunk_dict[key] = (line.replace(' switchport trunk allowed vlan ', '').rstrip())
#             elif 'access vlan' in line:
#                 access_dict[key] = (line.replace(' switchport access vlan ', '').rstrip())
#
#     ports_tuple = (access_dict, trunk_dict)
#     return ports_tuple
#
#
# print(get_int_vlan_map())
#
# vlan_str_list = line.replace(' switchport trunk allowed vlan ', '').rstrip().split(',')
# # print(vlan_str_list)
# vlan_list = []
# for _ in vlan_str_list:
#     vlan_list.append(int(_))
