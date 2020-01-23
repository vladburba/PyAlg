# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MAX_ITEM = 2
MIN_ITEM = 0
numbers1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
numbers2 = numbers1
print(numbers1)
print(numbers2)
# chislo = numbers2[0]
# print(chislo)
maxCount = 0
for numb1 in numbers1:
    chislo = numb1
    count = 0
    for numb2 in numbers2:
        if chislo == numb2:
            print(chislo, end=' = ')
            count += 1
            print(count, end=' ')
    print()
    if count >= maxCount:
        maxCount = count
        maxChislo = numb1
        # print(maxChislo)
print('Cлучай если другое число встретилось столько же раз не рассматриваем')
print(maxChislo, end=' Встретилось  = ')
print(maxCount)

