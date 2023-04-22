# Home worik seminar 6

import random

# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first = int(input("first>"))
q = int(input("q>"))
dif = int(input("dif>"))

list = []
for i in range(1, q + 1):
    next = first + (i - 1) * dif
    list.append(next)
print (list)

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

n = int(input("n>"))
m = int(input("m>"))

list = []
for i in range(10):
    list.append(random.randint(0, 9))

for i in range(len(list)):
    if list[i] >= n and list[i] <= m:
        print (i)
