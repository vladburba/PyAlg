# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def get_int_vlan_map(config_filename = 'config_sw2.txt'):
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


    ports_tuple = (access_dict, trunk_dict)
    return ports_tuple


print(get_int_vlan_map())
answer = get_int_vlan_map()
print(type(answer))

return_value = get_int_vlan_map('config_sw2.txt')
assert return_value != None, "Функция ничего не возвращает"
assert type(return_value) == tuple, "Функция должна возвращать кортеж"
assert len(return_value) == 2 and all(type(item) == dict for item in return_value), "Функция должна возвращать кортеж с двумя словарями"
# assert return_value == correct_return_value, "Функция возвращает неправильное значение"