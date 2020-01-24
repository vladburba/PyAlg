# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
# https://drive.google.com/file/d/1k0QZvlSKnwu8dVKrrEl6VHi6BsBvwps6/view?usp=sharing
a = int(input('Введите число а : '))
b = int(input('Введите число в : '))
c = int(input('Введите число с : '))

print(a,b,c)
if a > b:
    if a > c:
        if b > c:
            print(b)
        else:
            print(c)
    else:
        print(a)
else:
    if a > c:
        print(a)
    else:
        if b > c:
            print(c)
        else:
            print(b)
