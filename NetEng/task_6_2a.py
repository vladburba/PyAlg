ip_addr = input('Введите адрес IP-сети в формате: 10.1.1.0 ')

ip_addr_list = ip_addr.split('.')
print(ip_addr_list)
if len(ip_addr_list) == 4:
    try:
        ip_addr_oct1 = int(ip_addr_list[0], 10)
        ip_addr_oct2 = int(ip_addr_list[1], 10)
        ip_addr_oct3 = int(ip_addr_list[2], 10)
        ip_addr_oct4 = int(ip_addr_list[3], 10)
        print(ip_addr_oct1, ip_addr_oct2, ip_addr_oct3, ip_addr_oct4)
    except(ValueError):
        print('Неправильный IP-адрес')
    else:
        if 0 > ip_addr_oct1 or ip_addr_oct1 > 255:
            print('Неправильный IP-адрес')
        elif 0 > ip_addr_oct2 or ip_addr_oct2 > 255:
            print('Неправильный IP-адрес')
        elif 0 > ip_addr_oct3 or ip_addr_oct3 > 255:
            print('Неправильный IP-адрес')
        elif 0 > ip_addr_oct4 or ip_addr_oct4 > 255:
            print('Неправильный IP-адрес')
        elif 1 <= ip_addr_oct1 <= 223:
            print('unicast')
        elif 224 <= ip_addr_oct1 <= 239:
            print('multicast')
        elif ip_addr_oct1 == ip_addr_oct2 == ip_addr_oct3 == ip_addr_oct4 == 255:
            print('local broadcast')
        elif ip_addr_oct1 == ip_addr_oct2 == ip_addr_oct3 == ip_addr_oct4 == 0:
            print('unassigned')
        else:
            print('unused')
else:
    print('Неправильный IP-адрес')


