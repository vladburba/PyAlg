# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
# https://drive.google.com/file/d/1k0QZvlSKnwu8dVKrrEl6VHi6BsBvwps6/view?usp=sharing
a = str(input('Введите букву 1: '))
b = str(input('Введите букву 2: '))
print(ord(a))
print(ord(b))
if ord(a) > ord(b):
    print(ord(a) - ord(b) -1)
else:
    print(ord(b) - ord(a) -1)

