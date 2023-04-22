# Seminar 1
# БАЗОВЫЕ
# Task 1
print("Hello! What is your name?")
name = input("->")
print("How old are you?")
age = input("->")
print("Enter your sex?")
sex = input("->")
if sex == "male":
    print(f"Sir {name} is {age} years")
else:
    print(f"Lady {name} is {age} years")

# Task 2
print("Enter the timestamp")
timestamp = int(input("->"))
hours = timestamp//3600
minutes = timestamp//60
print(hours, ":", minutes, ":", timestamp)

# Task 3
print("Enter positive number")
n = int(input("->"))
print(f"{str(n)}{str(n+n)}{str(n+n+n)}")

#Task 4
print("Count enterprise finances")
positiv_balance = int(input("->"))
negativ_balance = int(input("->"))
pribil = positiv_balance-negativ_balance
rentability = 0
if pribil > 0:
    rentability = positiv_balance/negativ_balance
personal_amount = int(input("->"))
print(f"Pribil - {pribil}\nRentability - {rentability}\nPribil per personal - {pribil/personal_amount}")


# ДОПОЛНИТЕЛЬНЫЕ
# Task2
# Найдите сумму цифр трехзначного числа. 
print("Enter 3-digit number")
number = input("->")
if len(number) != 3:
    print("Entered number is not 3-digit number")
else:
    sum = 0
    i = 0
    while i < 3:
        sum += int(number[i])
        i += 1
print(sum)

# Task4
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
print("How mach birds did Petya, Kate and Sereja?")
number = int(input("->"))
# let x birds did Petay and x birds did Sereja, then 4x birds did Kate
if number % 6 == 0: 
    x = int(number / 6)
    print(f"Petya - {x}, Sereja - {x}, Kate - {4 * x}")
else: print("Something went wrong.")

# Task6
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
import random
ticket = random.randint(0, 1000000)
print(f"Funny ticket-{ticket}.")
first_number = ticket//1000
last_number = ticket%1000
def digit_sum(number):
    sum = 0
    sum += number//100
    number = number%100
    sum += number//10
    sum += number%10
    return sum
print("yes") if digit_sum(first_number) == digit_sum(last_number) else print("no")

# Task 8
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника). 
n = int(input("->"))
m = int(input("->"))
k = int(input("->"))
x = k/n
y = k/m
# проверяем на кратность и х меньше количества столбцов(возможность разделить)
if ((int(x) == x) and (x < m-1)) or ((int(y) == y) and (y < n-1)):
    print(n, m, k, ' -> yes')
else:
    print(n, m, k, ' -> no')
