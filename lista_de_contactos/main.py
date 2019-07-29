import os
from contact import Contact
from contacts_book import ContactBook


def continue_func():
    contin =str(input('\n-> Presione [enter] para continuar: '))


def add_contact_func(contact_book):
    os.system('clear')
    print('Anadir Contacto.\r\n')
    name = str(input('\t>Nombre: '))
    phone_number = str(input('\t>Telefono: '))
    e_mail = str(input('\t>Correo: '))
    contact_book.add_contact(name, phone_number, e_mail)
    continue_func()

def list_contact_func(contact_book):
    os.system('clear')
    contact_book.show_all()
    print('--- * --- * --- * --- * --- * --- * --- * ---')
    continue_func()

def delete_contact_func(contact_book):
    os.system('clear')
    name = str(input('>Nombre de contacto: '))
    contact_book.delete_contact(name)
    continue_func()

def search_contact_func(contact_book):
    os.system('clear')
    name = str(input('>Nombre de contacto: '))
    contact_book.search_contact(name)
    continue_func()

def update_contact_func(contact_book):
    os.system('clear')
    name = str(input('>Nombre de contacto: '))
    contact_book.update_contact(name)
    continue_func()


def command_select(command, contact_book):
    if command == 'anadir' or command == 'a':
        add_contact_func(contact_book)
    elif command == 'actuaizar' or command == 'ac':
        update_contact_func(contact_book)
    elif command == 'buscar' or command == 'b':
        search_contact_func(contact_book)
    elif command == 'eliminar' or command == 'e':
        delete_contact_func(contact_book)
    elif command == 'listar' or command == 'l':
        list_contact_func(contact_book)



def command_input():
    while True:
        os.system('clear')
        print('\tC O N T A C T O S.\r\n')
        command = str(input('>Qué deseas hacer? \n\t >[añadir] contacto.\n\t >[actualizar] contacto.\n\t >[buscar] contacto.\n\t >[eliminar] contacto.\n\t >[listar] contactos.\n\t >[salir].\n ->Opcion: ')).lower()
        if command == 'anadir' or command == 'actualizar' or command == 'buscar' or command == 'eliminar' or command == 'listar' or command == 'salir':
            break
        if command == 'a' or command == 'ac' or command == 'b' or command == 'e' or command == 'l' or command == 's':
            break
    return command



def main(command):
    contact_book = ContactBook()
    while True:
        if command == 'salir' or command == 's':
            break
        command_select(command, contact_book)
        command = command_input()

if __name__ == '__main__':
    command = command_input()
    main(command)
