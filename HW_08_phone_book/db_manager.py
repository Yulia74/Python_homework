from copy import deepcopy


phone_book = []
new_phone_book = []                                 # создали в конце работы для проверки save изменений
path ='phone_db.txt'

def open_file():
    global phone_book
    global new_phone_book
    global path
    with open(path, 'r', encoding='UTF-8') as file: # контекстный менеджер with сам 
        data = file.readlines()                     # закрывает файл
        for contact in data:                    # разобираем список строк на строки
            new = contact.strip().split(';')    # strip() очищает от псевдосимволов
            new_contact = {}                      # (лишних пробелов, \n, и т.д.)
            new_contact['name'] = new[0]
            new_contact['phone'] = new[1]
            new_contact['comment'] = new[2]
            phone_book.append(new_contact)      # добавляем в phone_book = []
    new_phone_book = deepcopy(phone_book)

def save_file():
    global phone_book
    global path
    data = []                                   # новая переменная
    for contact in phone_book:                   # contact.values - это значение (без values - ключи)
        data.append(';'.join(contact.values()))  # добавляем так, чтобы не было 
    data = '\n'.join(data)                       # \n после каждой записи, только между
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)                        # data должна быть такого же формата
        # как исходный файл phone_db.txt иначе вся программа поломается
        # строка, с разделителем ; и \n в конце


def get():                  # функция, возвращает нам справочник, ничего не принимает
    global phone_book       # через функцию, обращаемся к переменной
    return phone_book


def add(new_contact: dict):  # функция создать контакт, принимает (новую информацию: словарь)
    global phone_book
    phone_book.append(new_contact)


def find(find_option: str):
    global phone_book
    all_find = []
    for contact in phone_book:
        for element in contact.values():
            if find_option.lower() in element.lower():
                all_find.append(contact)    # записывает все, что находит похожее
    return all_find


def change_contact(ind: int, contact: dict):
    global phone_book
    phone_book.pop(ind-1)
    phone_book.insert(ind-1, contact)


def delete_contact(ind: int):
    global phone_book
    phone_book.pop(ind - 1)


def get_name(ind: int):
    global phone_book
    return phone_book[ind - 1].get('name')


def check_changes():
    global phone_book
    global new_phone_book
    if phone_book != new_phone_book:
        return True
    return False


# data = file.readlines() - возвращает список строк
# ['Кирилл Панфилов; 89094512021; GB\n', 'Андрей Мягкий; 89992223344; мастер-наладчик\n',
#   'Петр Первый; 777999000; старый знакомый']


# data = file.read() 
# Кирилл Панфилов; 89094512021; GB
# Андрей Мягкий; 89992223344; мастер-наладчик
# Петр Первый; 777999000; старый знакомый
# получаем строку, хотя она и разбита, все равно это одна строка
# и нам будет неудобно обращаться к словарю


# data = file.readline()
# Кирилл Панфилов; 89094512021; GB
# читает одну линию, эту команду надо использовать в цикле for

