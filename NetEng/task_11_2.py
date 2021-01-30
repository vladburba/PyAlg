# -*- coding: utf-8 -*-
'''
Задание 11.2

Создать функцию create_network_map, которая обрабатывает
вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну общую топологию.

У функции должен быть один параметр filenames, который ожидает как аргумент список с именами файлов, в которых находится вывод команды show cdp neighbors.

Функция должна возвращать словарь, который описывает соединения между устройствами.
Структура словаря такая же, как в задании 11.1:
    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}


Cгенерировать топологию, которая соответствует выводу из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

В словаре, который возвращает функция create_network_map, не должно быть дублей.

С помощью функции draw_topology из файла draw_network_graph.py нарисовать схему на основании топологии, полученной с помощью функции create_network_map.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Не копировать код функций parse_cdp_neighbors и draw_topology.

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''

import task_11_1

# import draw_network_graph

def create_network_map(filenames):
    sum_topo_dict = {}
    topo_dict = {}

    for _ in filenames:
        with open(_, 'r') as f:
            file_str = f.read()
            # print(file_str)
            # print(_, '=', task_11_1.parse_cdp_neighbors(file_str))
            topo_dict = (task_11_1.parse_cdp_neighbors(file_str))
            # print('topo_dict     =', topo_dict)
            sum_topo_dict.update(topo_dict)

    result_dict = {}
    print(sum_topo_dict)
    print(result_dict)

    for key, value in sum_topo_dict.items():

        if (key[0][0]) == 'S':
            result_dict[value] = key
            print(value, key)
        else:
            result_dict[key] = value
            print(key, value)

    print(result_dict)
    sum_topo_dict = result_dict.copy()
    result_dict = {}

    for sum_key, sum_value in sum_topo_dict.items():

        if result_dict.get(sum_value):
            print('Reverse_Duplication_found')

        else:
            result_dict[sum_key] = sum_value
            print('Add_new_element', sum_key, sum_value)

    for key, value in sum_topo_dict.items():
        print(key, value)

    print('-' * 40)

    print(result_dict)

    for key, value in result_dict.items():
        print(key, value)

    result_key = (sorted(result_dict))
    print(type(result_key))
    print(result_key)
    sort_dict = {}

    for key in result_key:
        sort_dict[key] = result_dict[key]

    print(sort_dict)

    for key, value in sort_dict.items():
        print(key, value)

    print(len(sort_dict))

    return sort_dict


if __name__ == '__main__':
    file_list = ['sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt']
    unified_return_value = create_network_map(file_list)
    print(unified_return_value)
    # draw_network_graph.draw_topology(unified_return_value)
