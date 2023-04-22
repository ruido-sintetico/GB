# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split()

start_str = 'a a a b c a a d c d d'
print(start_str)
start_str = start_str.split()

counts = {}

for char in start_str:
    if char in counts:
        counts[char] += 1
        print(f'{char}_{counts[char]}', end=' ')
    else:
        counts[char] = 0
        print(char, end=' ')


# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

# Output: 15

start_str = start_str.lower()
print(start_str)
start_str = start_str.split()
print(start_str)
print(set(start_str))
print(len(set(start_str)))



#

my_tuple = tuple([1, 1, 3, 4, 5])
my_lst = [1, 1, 3, 4, 5]
print(my_tuple.__sizeof__())
print(my_lst.__sizeof__())


my_dict = {
    (1, 2, 3): 'val'
}

print(my_dict[(1, 2, 3)])