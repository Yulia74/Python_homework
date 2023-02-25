'''Модуль контроллер - пусковой файл'''

import db_manager
import view 


def start():   
    while True:  
        choice = view.menu()                        # бесконечный цикл while, пока не введем 8
        match choice:                               # конструкция, заменяющая if, 
            case 1:                                 # но работающая, только с точными значениями
                db_manager.open_file()              # if работает с (=, >, <)
            case 2:
                db_manager.save_file()
            case 3:
                pb = db_manager.get()
                view.show_contacts(pb)
            case 4:
                new = view.new_contact_input()
                db_manager.add(new)                  # в db_meneger вызываем функцию add и передаем в нее new
            case 5:
                pb = db_manager.get()
                view.show_contacts(pb)
                ind = view.input_id()
                contact = view.new_contact_input()
                db_manager.change_contact(ind, contact)
            case 6:
                find = view.find_contact()           # то что мы ввели во view помещяется в переменную find 
                result = db_manager.find(find)
                view.show_contacts(result)           # еще раз воспользуемся f, чтобы показать result
            case 7:
                pb = db_manager.get()
                view.show_contacts(pb)
                ind = view.input_id()
                name = db_manager.get_name(ind)
                if view.confirm('удалить', name):
                    db_manager.delete_contact(ind)            
            case 8:
                if db_manager.check_changes():
                    if view.confirm_changes():
                        db_manager.save_file()
                print('До свидания!')
                break
            
                