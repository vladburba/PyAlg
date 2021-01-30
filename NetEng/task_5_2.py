# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


ip_net = input('Введите адрес IP-сети в формате: 10.1.1.0/24 ')
# ip_net = '10.1.1.0/24'
list_ip_net = ip_net.split('/')
Network = list_ip_net[0].split('.')
oct1 = int(Network[0])
oct2 = int(Network[1])
oct3 = int(Network[2])
oct4 = int(Network[3])

# print(Network)
print(f'''
Network:
{oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}
{oct1:08b} {oct2:08b} {oct3:08b} {oct4:08b}
''')

mask_dec = int(list_ip_net[1])
mask_bin = ('1' * mask_dec) + ('0' * (32 - mask_dec))
# print(mask_bin)

bin_oct1 = (mask_bin[0:8])
bin_oct2 = (mask_bin[8:16])
bin_oct3 = (mask_bin[16:24])
bin_oct4 = (mask_bin[24:32])
# print(bin_oct1)
# print(bin_oct2)
# print(bin_oct3)
# print(bin_oct4)
dec_oct1 = int(bin_oct1, 2)
dec_oct2 = int(bin_oct2, 2)
dec_oct3 = int(bin_oct3, 2)
dec_oct4 = int(bin_oct4, 2)
# print(oct1, oct2, oct3, oct4)

print(f'''
Mask:
/{mask_dec}
{dec_oct1:<8} {dec_oct2:<8} {dec_oct3:<8} {dec_oct4:<8}
{bin_oct1} {bin_oct2} {bin_oct3} {bin_oct4}
''')
