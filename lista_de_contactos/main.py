import os
import csv
from contact import Contact
from contacts_book import ContactBook
import os.path as path


def _continue_func():
    contin =str(input('\n-> Presione [enter] para continuar: '))


def add_contact_func(contact_book):
    os.system('clear')
    print('Anadir Contacto.\r\n')
    name = str(input('\t>Nombre: '))
    phone_number = str(input('\t>Telefono: '))
    e_mail = str(input('\t>Correo: '))
    contact_book.add_contact(name, phone_number, e_mail)
    print('\r\n\tNombre: {}, Telefone: {}, Correo: {}'.format(name, phone_number, e_mail))
    _continue_func()

def list_contact_func(contact_book):
    os.system('clear')
    contact_book.show_all()
    print('--- * --- * --- * --- * --- * --- * --- * ---')
    _continue_func()

def delete_contact_func(contact_book):
    os.system('clear')
    name = str(input('>Nombre de contacto: '))
    contact_book.delete_contact(name)
    _continue_func()

def search_contact_func(contact_book):
    os.system('clear')
    name = str(input('>Nombre de contacto: '))
    contact_book.search_contact(name)
    _continue_func()

def update_contact_func(contact_book):
    os.system('clear')
    name = str(input('>Nombre de contacto: '))
    contact_book.update_contact(name)
    _continue_func()


def _command_select(command, contact_book):
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



def _command_input():
    while True:
        os.system('clear')
        print('\tC O N T A C T O S.\r\n')
        command = str(input('>Qué deseas hacer? \n\t >[añadir]     contacto.\n\t >[actualizar] contacto.\n\t >[buscar]     contacto.\n\t >[eliminar]   contacto.\n\t >[listar]     contacto.\n\t >[salir].\n ->Opcion: ')).lower()
        if command == 'anadir' or command == 'actualizar' or command == 'buscar' or command == 'eliminar' or command == 'listar' or command == 'salir':
            break
        if command == 'a' or command == 'ac' or command == 'b' or command == 'e' or command == 'l' or command == 's':
            break
    return command



def main(command, contact_book):
    while True:
        if command == 'salir' or command == 's':
            break
        _command_select(command, contact_book)
        command = _command_input()

if __name__ == '__main__':
    contact_book = ContactBook()
    if path.exists(contact_book.FILE_NAME):
        with open(contact_book.FILE_NAME,'r') as file:
            reader = csv.reader(file)
            for idx,row in enumerate(reader):
                if idx != 0:
                    try:
                        contact_book.add_contact(row[0], row[1], row[2])
                    except IndexError:
                        continue
                else:
                    continue
    command = _command_input()
    main(command, contact_book)
