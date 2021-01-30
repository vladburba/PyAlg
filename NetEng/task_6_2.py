# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip_addr = input('Введите адрес IP-сети в формате: 10.1.1.0 ')

ip_addr_list = ip_addr.split('.')
ip_addr_oct1 = int(ip_addr_list[0], 10)
ip_addr_oct2 = int(ip_addr_list[1], 10)
ip_addr_oct3 = int(ip_addr_list[2], 10)
ip_addr_oct4 = int(ip_addr_list[3], 10)

if 1 <= ip_addr_oct1 <= 223:
    print('unicast')
elif 224 <= ip_addr_oct1 <= 239:
    print('multicast')
elif ip_addr_oct1 == ip_addr_oct2 == ip_addr_oct3 == ip_addr_oct4 == 255:
    print('local broadcast')
elif ip_addr_oct1 == ip_addr_oct2 == ip_addr_oct3 == ip_addr_oct4 == 0:
    print('unassigned')
else:
    print('unused')
