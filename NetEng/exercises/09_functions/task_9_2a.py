# -*- coding: utf-8 -*-
'''
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

trunk_mode_template = [
    'switchport mode trunk',
    'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}


def generate_trunk_config(intf_vlan_mapping, trunk_template):
    trunk_mode_dict = {}
    # print(trunk_mode_dict)
    for mode, vlans in intf_vlan_mapping.items():

        # print('interface {}'.format(mode))
        trunk_mode_list = []
        # print(vlans)
        vlan_str = str(vlans).lstrip('[').rstrip(']').replace(' ', '')
        # print(vlan_str)

        for command in trunk_template:
            if 'allowed vlan' in command:
                trunk_mode_list.append('{} {}'.format(command, vlan_str))
            else:
                trunk_mode_list.append(command)

            # print(command)
            # print(trunk_mode_list)
        #
        trunk_mode_dict['interface {}'.format(mode)] = trunk_mode_list
        # # print(trunk_mode_dict)

    return trunk_mode_dict


print(generate_trunk_config(intf_vlan_mapping=trunk_config, trunk_template=trunk_mode_template))


