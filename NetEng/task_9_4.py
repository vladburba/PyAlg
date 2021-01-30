# -*- coding: utf-8 -*-

ignore = ['duplex', 'alias', 'Current configuration']


def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return any(word in command for word in ignore)


def convert_config_to_dict(config_filename='config_sw1.txt'):
    '''
    Задание 9.4

    Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный файл коммутатора и возвращает словарь:
    * Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
    * Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
    * Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

    У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

    Проверить работу функции на примере файла config_sw1.txt

    При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!',
    а также строки в которых содержатся слова из списка ignore.

    Для проверки надо ли игнорировать строку, использовать функцию ignore_command.


    Ограничение: Все задания надо выполнять используя только пройденные темы.
    '''

    command_dict = {}
    with open(config_filename, 'r') as f:
        for line in f:
            if line == '\n':
                continue
            if line[0] == '!' or ignore_command(line, ignore) == True:
                continue
            elif line[0] != ' ':
                key = line.rstrip()
                # print(line.rstrip())
                command_dict[key] = []
                command_list = []
                # print(command_dict)
            elif line[0] == ' ':
                command_list.append(line.strip())
                # print(command_list)
                command_dict[key] = command_list

    return command_dict


print(convert_config_to_dict())
new_dict = convert_config_to_dict()

for key, value in new_dict.items():
    print(key, value)
