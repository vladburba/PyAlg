# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
# (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

import random

SIZE = 100
MAX_ITEM = 100
MIN_ITEM = 0
numbers = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range (SIZE)]
# numbers = [_ for _ in range(SIZE)]
positions = []
print(numbers)
print(positions)

for numb in numbers:
    if numb % 2 == 0:
        index_ = numbers.index(numb)
        # print(index)
        positions.append(index_)
print(positions)
