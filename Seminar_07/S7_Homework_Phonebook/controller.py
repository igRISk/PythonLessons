#import model_sum as model
#import model_sub as model
#import model_mult as model
import view


def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    model.init(value_a, value_b)
    result = model.get_result()
    view.view_data(result)


def open_file():
    path = input("Введите, пожалуйста, путь к файлу: ")
    phonebook = open(path, 'r')
    if '.xml' in path:
        
    if '.csv' in path:
        


def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
