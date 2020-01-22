# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

import random

# SIZE = 100
# MAX_ITEM = 100
# MIN_ITEM = 0
# array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range (SIZE)]
numbers = [_ for _ in range(2, 100)]
delitelys = [_ for _ in range(2, 10)]
print(numbers)
print(delitelys)
print(type(delitelys))
for delitel in delitelys:
    print(delitel, end='=')
    count = 0
    for numb in numbers:
        if numb % delitel == 0:
            count += 1
    print(count)
