# -*- coding: utf-8 -*-
'''
Задание 9.1a

Сделать копию функции из задания 9.1.

Дополнить скрипт:
* ввести дополнительный параметр, который контролирует будет ли настроен port-security
 * имя параметра 'psecurity'
 * по умолчанию значение None
 * для настройки port-security, как значение надо передать список команд port-security (находятся в списке port_security_template)

Функция должна возвращать список всех портов в режиме access
с конфигурацией на основе шаблона access_mode_template и шаблона port_security_template, если он был передан.
В конце строк в списке не должно быть символа перевода строки.


Проверить работу функции на примере словаря access_config,
с генерацией конфигурации port-security и без.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

access_mode_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

port_security_template = [
    'switchport port-security maximum 2',
    'switchport port-security violation restrict',
    'switchport port-security'
]

access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
}

def generate_access_config(intf_vlan_mapping, access_template, psecurity=None):
    '''
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/12':10,
         'FastEthernet0/14':11,
         'FastEthernet0/16':17}
    access_template - список команд для порта в режиме access

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    '''

    access_mode_list = []
    # print(access_mode_list)
    for mode, vlan in intf_vlan_mapping.items():
        # print('interface {}'.format(mode))
        access_mode_list.append('interface {}'.format(mode))
        # print(access_mode_list)
        for command in access_template:
            if 'access vlan' in command:
                access_mode_list.append('{} {}'.format(command, vlan))
            else:
                access_mode_list.append(command)
            # print(command)
            # print(access_mode_list)
        if psecurity:
            for command in psecurity:
                # print(command)
                access_mode_list.append(command)
                # print(access_mode_list)

    return access_mode_list

print(generate_access_config(intf_vlan_mapping=access_config, access_template=access_mode_template))
print(generate_access_config(intf_vlan_mapping=access_config, access_template=access_mode_template, psecurity=port_security_template))
