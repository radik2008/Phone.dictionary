import json

def menu():
    print('\x1b[1;3;5;31m   Main menu\x1b[0m')
    print('\x1b[32m1. Просмотреть контакты\x1b[0m')
    print('\x1b[32m2. Создать контакт\x1b[0m')
    print('\x1b[32m3. Удалить контакт\x1b[0m')
    print('\x1b[32m4. Найти контакт\x1b[0m')
    print('\x1b[32m5. Изменить контакт\x1b[0m')
    print('\x1b[32m6. Выход\x1b[0m')

def view_contacts():
    with open('contacts.json', 'r') as file:
        contacts = json.load(file)
    print("{:<20} {:<20} {:<20} {:<20}".format("Имя", "Фамилия", "Телефон", "Комментарий"))
    for contact in contacts:
        if "Comment" in contact:
            comment = contact["Comment"]
        else:
            comment = ""
        print("{:<20} {:<20} {:<20} {:<20}".format(contact["Name"], contact["Last Name"], contact["Phone number"], comment))

def create_contact():
    name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    phone_number = input("Введите номер телефона: ")
    comment = input("Введите комментарий (необязательно): ")

    new_contact = {"Name": name, "Last Name": last_name, "Phone number": phone_number}
    if comment:
        new_contact["Comment"] = comment

    with open("contacts.json", "r") as file:
        contacts = json.load(file)
    contacts.append(new_contact)

    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

    print("Контакт успешно создан")

def delete_contact():
    with open("contacts.json", "r") as data:
        contacts = json.load(data)
    name = input('\x1b[0;31mВведите имя или фамилию или телефон контакта, который хотите удалить: \x1b[0m').lower()
    new_contacts = []
    for contact in contacts:
        if name not in (contact['Name'] + contact['Last Name'] + contact['Phone number']).lower():
            new_contacts.append(contact)
    if len(new_contacts) < len(contacts):
        with open("contacts.json", "w") as data:
            json.dump(new_contacts, data)
        print("Контакт успешно удален")
        return
    print("\x1b[0;34mКонтакт не найден\x1b[0m")

def search_contact():
    with open("contacts.json", "r") as data:
        contacts = json.load(data)
    name_found = input('\x1b[0;31mВведите имя или фамилию или телефон контакта, который хотите найти: \x1b[0m').lower()
    found_contacts = {}
    for contact in contacts:
        if name_found in (contact['Name'] + contact['Last Name'] + contact['Phone number']).lower():
            found_contacts[contact['Name']] = contact
    for name, contact in found_contacts.items():
        if "Comment" in contact:
            comment = contact["Comment"]
        else:
            comment = ""
        print("{:<20} {:<20} {:<20} {:<20}".format(contact["Name"], contact["Last Name"], contact["Phone number"],
                                                   comment))
        return
    print("\x1b[0;34mКонтакт не найден\x1b[0m")

def edit_contact():
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
    name = input('\x1b[0;31mВведите имя контакта, который хотите изменить: \x1b[0m').lower()
    found_contact = None
    for contact in contacts:
        if str(contact["Name"]).lower() == name:
            found_contact = contact
            break
    if found_contact:
        new_name = input("Введите новое имя: ")
        new_last_name = input("Введите новую фамилию: ")
        new_phone_number = input("Введите новый номер телефона: ")
        new_comment = input("Введите новый комментарий (необязательно): ")

        found_contact["Name"] = new_name
        found_contact["Last name"] = new_last_name
        found_contact["Phone number"] = new_phone_number
        if new_comment:
            found_contact["Comment"] = new_comment

        with open("contacts.json", "w") as file:
            json.dump(contacts, file)

        print("Контакт успешно изменен")
    else:
        print("\x1b[0;34mКонтакт не найден\x1b[0m")

while True:
    menu()
    choice = input("\x1b[36mВведите номер меню: \x1b[0m")
    if choice == "1":
        view_contacts()
    elif choice == "2":
        create_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        search_contact()
    elif choice == "5":
        edit_contact()
    elif choice == "6":
        print('\x1b[1;31mВыход из программы\x1b[0m')
        break
    else:
        print('\x1b[1;31mНеверный выбор, попробуйте еще раз\x1b[0m')

