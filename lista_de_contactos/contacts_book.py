from contact import Contact
import csv

class ContactBook:
    FILE_NAME = 'contacts.csv'
    def __init__(self):
        self._contacts = []
        control_de_contacto_existente = False

    def add_contact(self, name, phone_number, e_mail):
        contact = Contact(name, phone_number, e_mail)
        self._contacts.append(contact)
        self._save()
        #print('name: {}, phone: {}, email: {}'.format(name, phone_number, e_mail))

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete_contact(self, name):
        control_de_contacto_existente = False
        for idx, contact in enumerate(self._contacts): #para iterar y que me devuelca el indice enumerate()
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                print('\n\tEliminado Exitosamente\r\n')
                control_de_contacto_existente = True
                break
            else:
                control_de_contacto_existente = False
        if control_de_contacto_existente == False:
            self._not_found()

    def search_contact(self, name):
        control_de_contacto_existente = False
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                control_de_contacto_existente = True
                break
            else:
                control_de_contacto_existente = False
        if control_de_contacto_existente == False:
            self._not_found()
        else:
            print('--- * --- * --- * --- * --- * --- * --- * ---')

    def update_contact(self, name):
        control_de_contacto_existente = False
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                control_de_contacto_existente = True
                break
            else:
                control_de_contacto_existente = False
        if control_de_contacto_existente == False:
            self._not_found()
        else:
            print('--- * --- * --- * --- * --- * --- * --- * ---')
            self._select_data_to_update(contact)

    def _select_data_to_update(self, contact):
        command = str(input('>Qué deseas hacer? \n\t >[nombre] del contacto.\n\t >[telefono] del contacto. \n\t >[correo] del contacto.\n ->Opcion: ')).lower()
        if command == 'nombre'or command == 'n':
            contact.name = str(input('>Ingrese el nuevo nombre: '))
        elif command == 'telefono' or command == 't':
            contact.phone_number = str(input('>Ingrese el nuevo telefono: '))
        elif command == 'correo' or command == 'c':
            contact.e_mail = str(input('>Ingrese el nuevo correo: '))
        else:
            self._not_found()
        self._save()

    def _save(self):
        with open(ContactBook.FILE_NAME,'w') as file:
            writer = csv.writer(file)
            writer.writerow(('name', 'phone_number', 'e_mail'))
            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone_number, contact.e_mail))

    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Nombre:   {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone_number))
        print('Correo:   {}'.format(contact.e_mail))
        #print('--- * --- * --- * --- * --- * --- * --- * ---')

    def _not_found(self):
        print('\t****************')
        print('\t No encontrado!')
        print('\t****************')
