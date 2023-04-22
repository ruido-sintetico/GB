# Seminar 2

# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random
n = int(input(">"))
coins = list([])
for el in range(n):
    c = random.randint(0,1)
    coins.extend([c])
print(coins)

count_up = 0
count_down = 0
for el in range(len(coins)):
    if coins[el] == 1:
        count_up += 1
    else:
        count_down += 1

if count_down > count_up: 
    print(count_up)
else: print(count_down)

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# Что бы решить эту задачу используем систему 2-х уравнений - (sum = x + y) и (mul = x * y).
# Таким образом задача сводится к решению уравнения - (ky^2 - sum*y + mul = 0) с последующим нахождением x.

import math
first = random.randint(0, 1000)
second = random.randint(0, 1000)

sum = first + second
mul = first * second
root = list([])
# D = sum**2 - 4*k*mul
D = sum**2 - 4*mul
if D < 0:
    print("Solution have no root")
elif D == 0:
    # a**2 - 4kb
    root.append([sum/2])
    print("sorry error")
else:
    root.append((sum + math.sqrt(D))/2)
    root.append((sum - math.sqrt(D))/2)
    print(root)
    print(first == root[0] or first == root[1])
    print(second == root[0] or second == root[1])

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input(">"))
exp_row = list([])
i = 0
while 2**i <= n:
    exp_row.append(2**i)
    i += 1
print(exp_row)

