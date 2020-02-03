# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
# https://drive.google.com/file/d/1eP3XSHS3I3UcQN4Tm4I2uUQEWPb-zu6V/view?usp=sharing

numb = int(input('Введите число: '))
obrat = 0
while numb > 0:
    obrat = obrat * 10 + numb % 10
    numb = numb // 10
print(obrat)