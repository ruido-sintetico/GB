# Задача No49.
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

PATH = "book.txt"

# Получаем файловый дескриптор телефонной книги


def get_phonebook(path):
    with open(path, "r") as df:
        return df.read()

# Вносим запись в телефонную книгу


def write_record_in_phonebook(path, record):
    # record = input("Enter contact in follow format: Фамилия Имя Отчество Телефон > ")
    with open(path, "a") as df:
        return df.write("\n" + record)

# Ищем записи по введенной строке


def search_in_pb(pb, search_object):
    # search_object = input("> ")
    recs = list(pb.split("\n"))
    found = []
    [found.append(i) for i in recs if i.find(search_object) != -1]
    return found

# Д/З
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

# Переписывает всю телефонную книгу в файл


def rewrite_book_in_file(pb, path):
    with open(path, "w") as df:
        df.write(pb)
        return df


def remove_record(pb, v):
    pb = list(pb.split("\n"))
    pb.remove(v)
    pb = "\n".join(pb)
    return pb


def change_record(pb, v1, v2):
    pb = remove_record(pb, v1)
    pb = pb.split('\n')
    pb.append(v2)
    pb = "\n".join(pb)
    return pb


command = input("Введите команду(\nshow,\nadd(\"Запись, которую необходимо добавить\"),\nsearch(\"шаблон поиска\"),\ndelete(\"запись для удаления\"),\nchange(\"Запись для удаления и запись для внесения\"))\n")
if command == "show":
    print(get_phonebook(PATH))
elif command == "delete":
    rec = input("Какую запись удалить\n")
    pb = get_phonebook(PATH)
    pb = remove_record(pb, rec)
    rewrite_book_in_file(pb, PATH)
elif command == "search":
    search = input(
        "Введите шаблон для поиска. Это может быть имя, фамилия, отчество или телефон или их фрагменты\n")
    pb = get_phonebook(PATH)
    res = search_in_pb(pb, search)
    print(res)
elif command == "change":
    pb = get_phonebook(PATH)
    v1 = input("Какую запись удалить\n")
    v2 = input("Какую запись добавить\n")
    pb = change_record(pb, v1, v2)
    rewrite_book_in_file(pb, PATH)
elif command == "add":
    v1 = input("Какую запись добавить\n")
    write_record_in_phonebook(PATH, v1)
