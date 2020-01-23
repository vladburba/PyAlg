# По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
# https://drive.google.com/file/d/1k0QZvlSKnwu8dVKrrEl6VHi6BsBvwps6/view?usp=sharing
x1 = int(input('Введите координаты х1 : '))
x2 = int(input('Введите координаты х2 : '))
y1 = int(input('Введите координаты y1 : '))
y2 = int(input('Введите координаты y2 : '))
print(x1,x2,y1,y2)
if x1 == x2:
    print('Нет решения')
else:
    if y1==y2:
        print('Нет решения')
    else:
        k = (y2 - y1)/(x2-x1)
        b = y1 - k*x1
        print(f'y = {k}x + {b}')



