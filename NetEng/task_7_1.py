# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

# O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0
# O        10.0.28.0/24 [110/31] via 10.0.13.3, 3d20h, FastEthernet0/0
# O        10.0.37.0/24 [110/11] via 10.0.13.3, 3d20h, FastEthernet0/0
# O        10.0.41.0/24 [110/51] via 10.0.13.3, 3d20h, FastEthernet0/0
# O        10.0.78.0/24 [110/21] via 10.0.13.3, 3d20h, FastEthernet0/0
# O        10.0.79.0/24 [110/20] via 10.0.19.9, 4d02h, FastEthernet0/2
# O        10.0.81.0/24 [110/41] via 10.0.13.3, 3d20h, FastEthernet0/0
# O        10.0.91.0/24 [110/60] via 10.0.19.9, 3d19h, FastEthernet0/2

# route_dict = {
#     'Protocol': '',
#     'Prefix': '',
#     'AD/Metric': '',
#     'Next-Hop': '',
#     'Last update': '',
#     'Outbound Interface': ''
# }
# print(route_dict)

with open('ospf.txt', 'r') as f:
    for line in f:
        # print(line.rstrip())
        line_list = line.split()
        # print(line_list)
        print('Protocol:           {} '.format('OSPF'))
        print('Prefix:             {} '.format(line_list[1]))
        print('AD/Metric:          {} '.format((line_list[2]).rstrip(']').lstrip('[')))
        print('Next-Hop:           {} '.format((line_list[4]).rstrip(',')))
        print('Last update:        {} '.format((line_list[5]).rstrip(',')))
        print('Outbound Interface: {} '.format((line_list[6]).rstrip(',')))
        print()
# print(f.closed)








