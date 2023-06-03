#Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, номер телефона - данные, которые должны находиться в файле.

path = 'phonebook.txt'
phonebook = []

# Проверка на существования файла
try:
    file = open(path, 'r')
except FileNotFoundError:
    file = open(path, 'w')
finally:
    file.close()

# Перезапись всех контактов
def rewrite():
    name = input('Enter a name: ')
    surname = input('Enter a surname: ')
    number = input('Enter the number: ')
    contact = {
        'name': name,
        'surname': surname,
        'number': number
    }
    phonebook.append(contact)

    with open(path, 'w') as data:
        for contact in phonebook:
            data.write(contact['name'] + ' ' + contact['surname'] + ': ' + contact['number'] + '\n')

# Добавление нового контакта
def add():
    name = input('Enter a name: ')
    surname = input('Enter a surname: ')
    number = input('Enter the number: ')
    contact = {
        'name': name,
        'surname': surname,
        'number': number
    }
    phonebook.append(contact)

    with open(path, 'a') as data:
        data.write(name + ' ' + surname + ': ' + number + '\n')

# Вывод всего списка 
def showall():
    if phonebook:
        print("Справочник:")
        for contact in phonebook:
            print(f"{contact['name']}, {contact['surname']}, {contact['number']}")
    else:
        print("Справочник пустой.")

# Обновление контакта по фамилии    
def update():
    surname = input('Enter the surname for update info: ')
    found = False
    for contact in phonebook:
        if contact['surname'] == surname:
            name = input('Enter a new name: ')
            number = input('Enter a new number: ')
            contact['name'] = name
            contact['number'] = number
            found = True
            break
    if found:
        with open(path, 'w') as data:
            for contact in phonebook:
                data.write(contact['name'] + ' ' + contact['surname'] + ': ' + contact['number'] + '\n')
        print('Contact updated.')
    else:
        print('Contact not found.')

# Удаление контакта
def delete():
    surname = input('Enter a surname to delete: ')
    found = False
    for contact in phonebook:
        if contact['surname'] == surname:
            phonebook.remove(contact)
            found = True
            break
    if found:
        with open(path, 'w') as data:
            for contact in phonebook:
                data.write(contact['name'] + ' ' + contact['surname'] + ': ' + contact['number'] + '\n')
        print('Contact deleted.')
    else:
        print('Contact not found.')

# Интерфейс взаимодействия пользователя
def user_choise():
    while True: # Постоянный вызов интерфейса
        choise = input('Select what do you want to do: \n'
                    ' 1 - Create new phonebook \n 2 - Add a number'
                    '\n 3 - Show all contacts \n 4 - Update contact \n'
                    ' 5 - Delete contact \n 0 - Exit \n')
        if choise == '1':
            rewrite()
        elif choise == '2':
            add()
        elif choise == '3':
            showall()      
        elif choise == '4':
            update()
        elif choise == '5':
            delete()
        elif choise == '0':
            break
        else:
            print('\n Incorrect command! :c \n')

# Вызов интерфейса
user_choise()
