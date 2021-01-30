# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv
ip_net = argv[1]

list_ip_net = ip_net.split('/')
Network = list_ip_net[0].split('.')
oct1 = int(Network[0])
oct2 = int(Network[1])
oct3 = int(Network[2])
oct4 = int(Network[3])

print(f'''
Network:
{oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}
{oct1:08b} {oct2:08b} {oct3:08b} {oct4:08b}
''')

mask_dec = int(list_ip_net[1])
mask_bin = ('1' * mask_dec) + ('0' * (32 - mask_dec))

bin_oct1 = (mask_bin[0:8])
bin_oct2 = (mask_bin[8:16])
bin_oct3 = (mask_bin[16:24])
bin_oct4 = (mask_bin[24:32])

dec_oct1 = int(bin_oct1, 2)
dec_oct2 = int(bin_oct2, 2)
dec_oct3 = int(bin_oct3, 2)
dec_oct4 = int(bin_oct4, 2)

print(f'''
Mask:
/{mask_dec}
{dec_oct1:<8} {dec_oct2:<8} {dec_oct3:<8} {dec_oct4:<8}
{bin_oct1} {bin_oct2} {bin_oct3} {bin_oct4}
''')
