# ДОПОЛНИТЕЛЬНЫЕ ЗАДАНИЯ:
# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

import random
N = int(input("N="))
numbers = list([])
while N > 0:
    numbers.append(random.randint(0, 9))
    N -= 1
x = int(input("x="))

print(numbers)
print(f"Решение задачи 1 - {numbers.count(x)}")

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
# Используем список и переменные из первой задачи

min = abs(x - numbers[0])
min_el = 0
for i in range(1, len(numbers)):
    if min > abs(x - numbers[i]):
        min = abs(x - numbers[i])
        min_el = i
print(F"Решение  задачи 2 - {min_el}, {min}")

# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# *Пример:*
# ноутбук - 12

word = input("word>").upper()
lang = ""
sum = 0
for s in range(len(word)):
    # Check what alphabets we are using
    if ord(word[s]) >= ord("А") and ord(word[s]) <= ord("я"):
        if lang == "":
            lang = "ru"
        elif lang == "en":
            raise Exception(
                "Word consist from symbols from different alphabets")
    elif ord(word[s]) >= ord("A") and ord(word[s]) <= ord("z"):
        if lang == "":
            lang = "en"
        elif lang == "ru":
            raise Exception(
                "Word consist from symbols from different alphabets")
    else:
        print("unknown alphabet")

ru_alphabet = (
    (1, "А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"),
    (2, "Д", "К", "Л", "М", "П", "У"),
    (3, "Б", "Г", "Ё", "Ь", "Я"),
    (4, "Й", "Ы"),
    (5, "Ж", "З", "Х", "Ц", "Ч"),
    (8, "Ш", "Э", "Ю"),
    (10, "Ф", "Щ", "Ъ")
)

en_alphabet = (
    (1, "A", "E", "I", "O", "U", "L", "N", "S", "T", "R"),
    (2, "D", "G"),
    (3, "B", "C", "M", "P"),
    (4, "F", "H", "V", "W", "Y"),
    (5, "K"),
    (8, "J", "X"),
    (10, "Q", "Z")
)

if lang == "ru":
    # Take symbol in word
    for letter in range(len(word)):
        # Parsed lists of alphabet symbols
        for letters_list in range(len(ru_alphabet)):
            # Check letter in list alphabet simbols
            if word[letter] in ru_alphabet[letters_list]:
                # Summarize
                sum += ru_alphabet[letters_list][0]

if lang == "en":
    # Take symbol in word
    for letter in range(len(word)):
        # Parsed lists of alphabet symbols
        for letters_list in range(len(en_alphabet)):
            # Check letter in list alphabet simbols
            if word[letter] in en_alphabet[letters_list]:
                # Summarize
                sum += en_alphabet[letters_list][0]
print(sum)

# БАЗОВЫЕ ЗАДАНИЯ:
# ""
# 1. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите два варианта решения: через list и через dict.

# Пример:
# Введите номер месяца: 10
# Результат через список: Осень
# Результат через словарь: Осень

month = int(input("month>"))
if month > 1 and month < 12:
    monthes_list = ["january", "february", "march", "april", "may", "june",
                    "july", "august", "september", "octouber", "november", "december"]
    monthes_dict = {1: "january",
                    2: "february",
                    3: "march",
                    4: "april",
                    5: "may",
                    6: "june",
                    7: "july",
                    8: "august",
                    9: "september",
                    10: "octouber",
                    11: "november",
                    12: "december"}

    # for list
    i = monthes_list[month - 1]
    if i == "december" or i == "january" or i == "february":
        print("Winter")
    elif i == "may" or i == "april" or i == "march":
        print("Spring")
    elif i == "june" or i == "july" or i == "august":
        print("Summer")
    else:
        print("autemn")

    # for dictionary
    i = monthes_dict[month]
    if i == "december" or i == "january" or i == "february":
        print("Winter")
    elif i == "may" or i == "april" or i == "march":
        print("Spring")
    elif i == "june" or i == "july" or i == "august":
        print("Summer")
    else:
        print("autemn")
else:
    print("Enter number from 1 to 12")

# 2. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль (try except).

# Пример:
# Введите первое число: 10
# Введите второе число: 0
# Вы что? Пытаетесь делить на 0!

# Пример:
# Введите первое число: 10
# Введите второе число: 10
# 1.0

nominator = int(input("n>"))
denominator = int(input("d>"))


def devision(n, m):
    try:
        print(n/m)
    except:
        print("Devision by zero")


devision(nominator, denominator)


# 3. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# Пример:
# Иван Иванов 1846 года рождения, проживает в городе Москва,
# email: jackie@gmail.com, телефон: 01005321456

name = input("name>")
sirname = input("sirname>")
year = input("year>")
live_in = input("live in>")
email = input("email>")
phone = input("phone>")


def who_is_it(name, sirname, year_of_birth, live_in, email, phone):
    print(f"{name} {sirname} {year_of_birth} года рождения, проживает в городе {live_in}, email:{email}, телефон: {phone}")


who_is_it(name, sirname, year, live_in, email, phone)

# 4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
# Попробуйте решить задачу двумя способами:
# 1) используя функцию sort()
# 2) без функции sort()

a = int(input("a>"))
b = int(input("b>"))
c = int(input("c>"))


def my_func_without_sort(*args):
    if a > b and a > c and b > c:
        print(a + b)
    elif a > b and a > c and b < c:
        print(a + c)
    if b > a and b > c and a > c:
        print(b + a)
    elif b > a and b > c and a < c:
        print(b + c)
    if c > a and c > b and a > b:
        print(c + a)
    elif c > a and c > b and a < b:
        print(c + b)


my_func_without_sort(a, b, c)


def my_func_with_sorted(*args):
    sorted_list = sorted(args)
    print(sorted_list[-1] + sorted_list[-2])


my_func_with_sorted(a, b, c)


def my_func_with_sort(*args):
    list_ = list(args)
    list_.sort()
    print(list_[-1] + list_[-2])


my_func_with_sort(a, b, c)
