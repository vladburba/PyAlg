# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# https://drive.google.com/file/d/1k0QZvlSKnwu8dVKrrEl6VHi6BsBvwps6/view?usp=sharing

d = int(input('Введите трехзначное целое число: '))
# процесс
a = d // 100
b = (d // 10) - (a * 10)
c = d - (a * 100) - (b * 10)
sum = a + b + c
mult = a * b * c
print(sum)
print(mult)


