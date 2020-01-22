# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 100
MAX_ITEM = 100
MIN_ITEM = 0
numbers = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(numbers)
min_ = numbers[0]
max_ = numbers[0]
# print(max_)
# print(min_)
for numb in numbers:
    if min_ > numb:
        min_ = numb
for numb in numbers:
    if max_ < numb:
        max_ = numb

pos_min = numbers.index(min_)
pos_max = numbers.index(max_)
print(max_, end=' = ')
print(pos_max)
print(min_, end=' = ')
print(pos_min)
numbers.insert(pos_min, max_)
numbers.insert(pos_max, min_)
print(numbers)


