# Напишите проект, содержащий функционал работы с заметками.
# Программа должна уметь создавать заметку, сохранять её
# , читать список заметок, редактировать заметку, удалять заметку.
import os


def create_note():
    head = input("Введите название заметки:\n")
    body = input("Вводите заметку:\n")
    return head, body


def save_note(head, body):
    filepath = "C:\\Users\\Ivanlogin888\\Desktop\\notice\\" + head + ".txt"
    if os.path.exists(head + ".txt"):
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(body)
            return print(f'Данные были успешно добавлены!')
    else:
        with open(filepath, 'w+', encoding='utf-8') as f:
            f.write(body)
            return print(f'Данные были успешно сохранены!')


def read_note():
    head = input('Введите Название заметки\n')
    filepath = "C:\\Users\\Ivanlogin888\\Desktop\\notice\\" + head + ".txt"
    if os.path.exists(head + ".txt"):
        with open(filepath, 'r+', encoding='utf-8') as f:
            for line in f:
                print(line)
    else:
        return print(f'Файла с названием {head}.txt не существует')
def del_note():
    head = input('Введите Название заметки\n')
    filepath = "C:\\Users\\Ivanlogin888\\Desktop\\notice\\" + head + ".txt"
    if os.path.isfile(filepath):
        os.remove(filepath)
        print("Удаление прошло успешно")
    else:
        print("Файла с названием {head}.txt не существует")



def choose():
    while True:
        choise = input('Введите действие (1,2,3,4,5) -> ')
        if choise == '1': head, body = create_note()
        elif choise == '2': return save_note(head, body)
        elif choise == '3': return read_note()
        elif choise == '4': return del_note()
        elif choise == '5': exit()


while True:
    print('Выберите действие: \n 1 - Создать заметку \n 2 - Сохранить заметку'
          ' \n 3 - Прочитать заметку  \n 4 - Удалить заметку \n 5 - Выход ')
    choose()
    input('Введите ENTER чтобы продолжить!')
