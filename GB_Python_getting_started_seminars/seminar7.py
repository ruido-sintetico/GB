# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам

phrases = (input("> ").upper().split(" "))
print(phrases)
glasnie = ("А", "О", "Я", "Ё", "У", "Ю", "Е", "Э", "И", "Ы")

# Функция, которая возвращает массив, в котором удалены согласные буквы


def get_only_glasnie(phrases, glasnie):
    only_glasnie = []
    for i in phrases:
        only_glasnie.append(list(filter(lambda x: x in glasnie, i)))
    return only_glasnie

# Функция, проверяет список списков, полученный в функции get_only_glasnie. Если все списки одинаковой длины, то ритм есть.


def is_it_rythm(only_glasnie):
    len_zero_element = len(only_glasnie[0])
    for j in range(1, len(only_glasnie)):
        if len(only_glasnie[j]) != len_zero_element:
            return False
    return True


gl = get_only_glasnie(phrases, glasnie)

if is_it_rythm(gl):
    print("Парам пам-пам")
else:
    print("Пам парам")

# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента,
# как, например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) `
# **Вывод:**

# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36


def operation(x, y): return x*y


def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(f"{operation(i, j)}, ", end="")
        print("")


print_operation_table(operation, 8, 8)