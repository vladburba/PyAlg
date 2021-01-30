# -*- coding: utf-8 -*-
"""
Задание 12.3


Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.


Для этого задания нет тестов
"""


def my_print_ip_table(reachable, unreachable):
    from tabulate import tabulate

    columns = ['Reachable', 'Unreachable']
    len_reach = len(reachable)
    len_unr = len(unreachable)

    if len_reach > len_unr:
        for _ in range(len_unr, len_reach):
            unreachable.append('')

    elif len_reach < len_unr:
        for _ in range(len_reach, len_unr):
            reachable.append('')

    list_of_lists = zip(reachable, unreachable)
    # print(list_of_lists)
    print(tabulate(list_of_lists, headers=columns))


if __name__ == '__main__':
    list1 = ['10.1.1.1', '10.1.1.2', '10.1.1.3']
    list2 = ['10.1.1.7', '10.1.1.8', '10.1.1.9', '10.1.1.10', '10.1.1.11']
    my_print_ip_table(list1, list2)
