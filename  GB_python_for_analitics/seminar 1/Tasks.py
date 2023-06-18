# Условие 1:
# Оформляйте ноутбук, используя эти советы:
# Номер задачи - заголовок 2
# Номер подзадачи - заголовок 3
# Предоставленные наборы данных оформляйте, как код
# Рекомендации для преподавателей по оценке задания:
# Смотреть, чтобы студент красиво оформлял ноутбук, использовал ячейки с текстом, указывал номера заданий

# Условие 2:
# На складе лежат разные фрукты в разном количестве.
# Нужно написать функцию, которая на вход принимает любое количество названий фруктов и их количество, а возвращает общее количество фруктов на складе

fruits = {}
while True:
  fruits_name = input("name>")
  if fruits_name == "":
    break
  fruits_number = int(input("num>"))
  fruits[fruits_name] = fruits_number

def get_sum_of_fruits ( frs = {"fruits": 0} ) -> int:
  sum = 0
  for i in frs:
    sum = sum + frs[i]
  return sum
print(get_sum_of_fruits(fruits))

# Условие 3:
# Дан список с затратами на рекламу. Но в данных есть ошибки, некоторые затраты имеют отрицательную величину. Удалите такие значения из списка и посчитайте суммарные затраты
# [100, 125, -90, 345, 655, -1, 0, 200]
# Используйте list comprehensions

costs = [100, 125, -90, 345, 655, -1, 0, 200] 
positive_costs = [i for i in costs if i > 0]
sum = 0
for i in positive_costs:
  sum+=i
print(sum)

# Условие 4.1:
# Даны два списка.
# Дата покупки
# ['2021-09-14', '2021-12-15', '2021-09-08', '2021-12-05', '2021-10-09', '2021-09-30', '2021-12-22', '2021-11-29', '2021-12-24', '2021-11-26', '2021-10-27', '2021-12-18', '2021-11-09', '2021-11-23', '2021-09-27', '2021-10-02', '2021-12-27', '2021-09-20', '2021-12-13', '2021-11-01', '2021-11-09', '2021-12-06', '2021-12-08', '2021-10-09', '2021-10-31', '2021-09-30', '2021-11-09', '2021-12-13', '2021-10-26', '2021-12-09']
# Суммы покупок по датам
# [1270, 8413, 9028, 3703, 5739, 4095, 295, 4944, 5723, 3701, 4471, 651, 7037, 4274, 6275, 4988, 6930, 2971, 6592, 2004, 2822, 519, 3406, 2732, 5015, 2008, 316, 6333, 5700, 2887]

dates_of_purchase = ['2021-09-14', '2021-12-15', '2021-09-08', '2021-12-05', '2021-10-09', '2021-09-30', '2021-12-22', '2021-11-29', '2021-12-24', '2021-11-26', '2021-10-27', '2021-12-18', '2021-11-09', '2021-11-23', '2021-09-27', '2021-10-02', '2021-12-27', '2021-09-20', '2021-12-13', '2021-11-01', '2021-11-09', '2021-12-06', '2021-12-08', '2021-10-09', '2021-10-31', '2021-09-30', '2021-11-09', '2021-12-13', '2021-10-26', '2021-12-09']
sums_of_purchase = [1270, 8413, 9028, 3703, 5739, 4095, 295, 4944, 5723, 3701, 4471, 651, 7037, 4274, 6275, 4988, 6930, 2971, 6592, 2004, 2822, 519, 3406, 2732, 5015, 2008, 316, 6333, 5700, 2887]

# 4.1 Найдите, какая выручка у компании в ноябре
# Используйте list comprehensions

get_monthes = [i.split("-")[1] for i in dates_of_purchase]
costs_of_november = [sums_of_purchase[i] for i in range(len(sums_of_purchase)) if get_monthes[i] == '11']
sum = 0
def get_sums (costs, sum = 0) -> int:
  for i in costs:
    sum += i
  return sum
print (get_sums(costs_of_november))

# 4.2 Найдите выручку компании в зависимости от месяца
# Для этого напишите функцию, которая на вход принимает список с датами и список с выручкой, а на выходе словарь, где ключи - это месяцы, а значения - это выручка.
# Используйте аннотирование типов.

monthes = {"september": "09", "october": "10", "november": "11", "december": "12"}
def amount_of_month(ms: dict, dates: list, sums: list) -> dict:
  result = {"september": 0, "october": 0, "november": 0, "december": 0}
  for i in ms:
    for j in range(len(dates)):
      month_number = dates[j].split("-")[1]
      if month_number == ms[i]:
        result[i] = result[i] + sums[j]
  return result
print(amount_of_month(monthes, dates_of_purchase, sums_of_purchase))