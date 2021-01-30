# -*- coding: utf-8 -*-
'''
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


ip_addr = input('Введите адрес IP-сети в формате: 10.1.1.0/24 ')
# ip_addr = '127.127.127.127/29'
list_ip_addr = ip_addr.split('/')
# print(list_ip_addr[0])
# print(list_ip_addr[1])

host = list_ip_addr[0].split('.')
host_oct1_dec = int(host[0], 10)
host_oct2_dec = int(host[1], 10)
host_oct3_dec = int(host[2], 10)
host_oct4_dec = int(host[3], 10)
host_bin = '{:08b}'.format(host_oct1_dec) + '{:08b}'.format(host_oct2_dec) \
           + '{:08b}'.format(host_oct3_dec) + '{:08b}'.format(host_oct4_dec)
# print(host_bin)

mask_dec = int(list_ip_addr[1], 10)
mask_bin = ('1' * mask_dec) + ('0' * (32 - mask_dec))
mask_oct1_bin = mask_bin[0:8]
mask_oct2_bin = mask_bin[8:16]
mask_oct3_bin = mask_bin[16:24]
mask_oct4_bin = mask_bin[24:32]
mask_oct1_dec = int(mask_oct1_bin, 2)
mask_oct2_dec = int(mask_oct2_bin, 2)
mask_oct3_dec = int(mask_oct3_bin, 2)
mask_oct4_dec = int(mask_oct4_bin, 2)
# print(mask_bin)


net_bin = host_bin[0:mask_dec] + ('0' * (32 - mask_dec))
# print(net_bin)
net_oct1_bin = net_bin[0:8]
net_oct2_bin = net_bin[8:16]
net_oct3_bin = net_bin[16:24]
net_oct4_bin = net_bin[24:32]
net_oct1_dec = int(net_oct1_bin, 2)
net_oct2_dec = int(net_oct2_bin, 2)
net_oct3_dec = int(net_oct3_bin, 2)
net_oct4_dec = int(net_oct4_bin, 2)

print(f'''
Network:
{net_oct1_dec:<8} {net_oct2_dec:<8} {net_oct3_dec:<8} {net_oct4_dec:<8}
{net_oct1_bin} {net_oct2_bin} {net_oct3_bin} {net_oct4_bin} 
''')

print(f'''
Mask:
/{mask_dec}
{mask_oct1_dec:<8} {mask_oct2_dec:<8} {mask_oct3_dec:<8} {mask_oct4_dec:<8} 
{mask_oct1_bin} {mask_oct2_bin} {mask_oct3_bin} {mask_oct4_bin}
''')
