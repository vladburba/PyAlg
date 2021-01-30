# -*- coding: utf-8 -*-
#!/usr/bin/env python3

while True:

    try:
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
        mask_dec = int(list_ip_addr[1], 10)
        host_bin = '{:08b}'.format(host_oct1_dec) + '{:08b}'.format(host_oct2_dec) \
                   + '{:08b}'.format(host_oct3_dec) + '{:08b}'.format(host_oct4_dec)
        host_oct1_bin = host_bin[0:8]
        host_oct2_bin = host_bin[8:16]
        host_oct3_bin = host_bin[16:24]
        host_oct4_bin = host_bin[24:32]
        mask_bin = ('1' * mask_dec) + ('0' * (32 - mask_dec))
        mask_oct1_bin = mask_bin[0:8]
        mask_oct2_bin = mask_bin[8:16]
        mask_oct3_bin = mask_bin[16:24]
        mask_oct4_bin = mask_bin[24:32]
        mask_oct1_dec = int(mask_oct1_bin, 2)
        mask_oct2_dec = int(mask_oct2_bin, 2)
        mask_oct3_dec = int(mask_oct3_bin, 2)
        mask_oct4_dec = int(mask_oct4_bin, 2)
        net_bin = host_bin[0:mask_dec] + ('0' * (32 - mask_dec))
        net_oct1_bin = net_bin[0:8]
        net_oct2_bin = net_bin[8:16]
        net_oct3_bin = net_bin[16:24]
        net_oct4_bin = net_bin[24:32]
        net_oct1_dec = int(net_oct1_bin, 2)
        net_oct2_dec = int(net_oct2_bin, 2)
        net_oct3_dec = int(net_oct3_bin, 2)
        net_oct4_dec = int(net_oct4_bin, 2)

    except(Exception):
        print("Что-то пошло не так...")
        my_exit = input('Зкончим - (q): ')
        if my_exit == 'q':
            break
    else:
        if (0 <= host_oct1_dec <= 255) and (0 <= host_oct2_dec <= 255) and (0 <= host_oct3_dec <= 255) and (
                0 <= host_oct4_dec <= 255 and (0 <= mask_dec <= 32)):
            print('Host_bin:', host_bin)
            print('Mask_bin:', mask_bin)
            print('Netw_bin:', net_bin)

            print(
                f'''Host:     {host_oct1_dec:<8} {host_oct2_dec:<8} {host_oct3_dec:<8} {host_oct4_dec:<8}\n {host_oct1_bin:>17} {host_oct2_bin} {host_oct3_bin} {host_oct4_bin} ''')

            print(
                f'''Mask/{mask_dec:<2}:  {mask_oct1_dec:<8} {mask_oct2_dec:<8} {mask_oct3_dec:<8} {mask_oct4_dec:<8}\n {mask_oct1_bin:>17} {mask_oct2_bin} {mask_oct3_bin} {mask_oct4_bin}''')

            print(
                f'''Network:  {net_oct1_dec:<8} {net_oct2_dec:<8} {net_oct3_dec:<8} {net_oct4_dec:<8}\n {net_oct1_bin:>17} {net_oct2_bin} {net_oct3_bin} {net_oct4_bin} ''')

            my_exit = input('Продолжим - (y): ')
            if my_exit == 'y':
                continue
            else:
                break

        else:
            print("Что-то пошло не так...")
            my_exit = input('Зкончим - (q): ')
            if my_exit == 'q':
                break
    finally:
        print("Работа завершена!")
