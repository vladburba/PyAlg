# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
# https://drive.google.com/file/d/1eP3XSHS3I3UcQN4Tm4I2uUQEWPb-zu6V/view?usp=sharing

num = int(input('Введите число: '))
chet = 0
nechet = 0
while num > 0:
    if num % 2 == 0:
        chet +=1
    else:
        nechet+=1
    num = num // 10
print('Четных чисел = ', chet)
print('Нечетных чисел = ', nechet)
