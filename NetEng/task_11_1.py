# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def parse_cdp_neighbors(command_output):

    topology_dict = {}
    # print(command_output, sep='')


    first_line_id = command_output.find('Port ID\n') + 8
    new_str = command_output[first_line_id:]
    # print('first_line_id:', first_line_id)
    # print('new_str = ', new_str, sep='|')

    str_list = new_str.split('\n')
    str_list.remove('')
    # print('str_list = ', str_list)
    device = command_output[0:command_output.find('>')]
    # print('dev_name =', device)

    my_str_list = []
    for my_str in str_list:
        my_str_list.append(my_str.split(' '))
        # print('my_str_list = ', my_str_list)


    for elem in my_str_list:
        # print('el:', elem)
        neighbor = elem[0]
        elem.remove(neighbor)
        # print(elem)

        neigh_int = elem[-2] + elem[-1]
        ind = 0
        for char in elem:
            ind += 1

            if char != '':

                # print('ind=', ind)
                # print('char=', char)
                break

        # print(elem[ind-1], elem[ind], elem[ind+1] )
        dev_int = elem[ind-1] + elem[ind]
        # print('dev_name =', device)
        # print('device_interface =', dev_int)
        # print('neighbor =', neighbor)
        # print('neighbor_int', neigh_int)

        topology_dict[(device, dev_int)] = (neighbor, neigh_int)
        # print(topology_dict)



    # print('topology_dict =', topology_dict)

    return topology_dict


if __name__ == '__main__':
    with open('sh_cdp_n_sw1.txt', 'r') as f:
        file_str = f.read()
        # print('main_progrgam file_str:', file_str)

    for key, value in parse_cdp_neighbors(file_str).items():
        print(key, value)


    # print('main_programm =', parse_cdp_neighbors(file_str))

