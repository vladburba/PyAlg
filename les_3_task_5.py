# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# # Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# # Это два абсолютно разных значения.
import random

SIZE = 10
MAX_ITEM = 1
MIN_ITEM = -5
numbers = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(numbers)

for numb in numbers:
    if numb < 0:
        max_elem = numb
# print(max_elem)

for numb in numbers:
    if numb < 0:
        if max_elem < numb:
            max_elem = numb
print(max_elem)
