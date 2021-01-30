"""
Создаем yaml файл со списком всех активных сетевых устройств в сети
"""
str1 = '- device_type: cisco_ios'
str2 = '  ip: 192.168.x.y'
str3 = '  username: vlad'
str4 = '  password: Genom1111'

if __name__ == '__main__':
    for i in range(0, 51):
        line = str2.replace('x', str(i))
        print(line)
        for j in range(245, 251):
            line2 = line.replace('y', str(j))
            with open('all_dev_list.yaml', 'a') as f:
                f.write(str1+'\n')
                f.write(line2+'\n')
                f.write(str3+'\n')
                f.write(str4+'\n')
