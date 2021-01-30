# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""


def convert_ios_nat_to_asa(ios_nat, asa_nat):
    import re
    with open(ios_nat, 'r') as src, open(asa_nat, 'w') as dst:
        for line in src:
            print(line.rstrip())
            match = re.search(r'ip nat inside source static tcp (\S+) (\S+) interface \S+ (\S+)', line)
            ip = match.group(1)
            port1 = match.group(2)
            port2 = match.group(3)
            print(ip, port1, port2)
            asa_str1 = 'object network LOCAL_' + ip + '\n'
            dst.write(asa_str1)
            asa_str2 = ' host ' + ip + '\n'
            dst.write(asa_str2)
            asa_str3 = ' nat (inside,outside) static interface service tcp {} {}\n'.format(port1, port2)
            dst.write(asa_str3)

    return None


if __name__ == '__main__':
    ios = 'cisco_nat_config.txt'
    asa = 'asa_nat_config.txt'

    convert_ios_nat_to_asa(ios, asa)
