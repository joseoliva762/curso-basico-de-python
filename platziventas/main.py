
import os

def create_client(client, client_list):
    if client not in client_list:
        client_list.append(client)
    else:
        print('\nEl cliente ya esta en la lista.\n')
    return client_list

def list_client(client_list):
    print('\n')
    _separete()
    print('\t\t---->> L I S T A   D E   C L I E N T E S. <<----')
    _separete()
    print('\n')
    for idx, client in enumerate(client_list):
        _print_client(idx, client)
    print('\n')
    _separete()

def update_client(client_name, client_list):
    _separete()
    for idx, client in enumerate(client_list):
        if client_list[idx]['name'].lower() == client_name.lower():
            _print_client(idx, client)
            _separete()
            print('\n')
            while True:
                client_list = _select_data_to_update(idx, client_list)
                _separete()
                if  _updata_again().lower() == 'n':
                    break
                _separete()
            break
    else:
        _not_found()
    return client_list


def delete_client(client_name, client_list):
    for idx, client in enumerate(client_list):
        if client_list[idx]['name'].lower() == client_name.lower():
            del client_list[idx]
            print('\n\tEliminado Exitosamente\r\n')
            break
    else:
        _not_found()
    return client_list


def search_client(client_name, client_list):
    for idx, client in enumerate(client_list):
        if client_list[idx]['name'].lower() == client_name.lower():
            _print_client(idx, client)
            break
    else:
        _not_found()


def _updata_again():
    return str(input('Desea continuar Actualizando los datos? [s/n]: '))


def _select_data_to_update(idx, client_list):
    command = str(input('>Qué deseas actualizar? \n\t >[nombre] del cliente.\n\t >[compañia] del cliente. \n\t >[correo] del cliente.\n\t >[posicion] del cliente.\n\t >[salir]\n ->Opcion: ')).lower()
    if command.lower() == 'nombre'or command.lower() == 'n':
        client_list[idx]['name'] = str(input('>Ingrese el nuevo nombre: '))
    elif command.lower() == 'compañia' or command.lower() == 'com':
        client_list[idx]['compañia'] = str(input('>Ingrese la nueva compañia: '))
    elif command.lower() == 'correo' or command.lower() == 'c':
        client_list[idx]['correo'] = str(input('>Ingrese el nuevo correo: '))
    elif command.lower() == 'posicion' or command.lower() == 'p':
        client_list[idx]['posicion'] = str(input('>Ingrese el nuevo puesto: '))
    return client_list



def _not_found():
    _separete()
    print('\t\t               >>No encontrado!<<               ')
    _separete()


def _get_client_field(field_name):
    field = None
    while not field:
        field = str(input('Cual es el {} del cliente: '.format(field_name)))
    return field


def _client_data():
    client = {
        'name': _get_client_field('nombre'),
        'compañia': _get_client_field('compañia'),
        'correo': _get_client_field('correo'),
        'posicion': _get_client_field('posicion')
    }
    return client

def _command_insert():
    _print_welcome()
    return str(input('Que quiere hacer hoy?\n\t >[crear]      cliente.\n\t >[eliminar]   cliente.\n\t >[actualizar] cliente.\n\t >[buscar]     cliente.\n\t >[listar]     cliente.\n\t >[salir]\n Opcion: '))

def _command_select(command, client_list):
    os.system('clear')
    _print_welcome()
    if command.lower() == 'crear' or command.lower() == 'c':    
        client = _client_data()
        if client != None:
            client_list = create_client(client, client_list)
        list_client(client_list)
    elif command.lower() == 'eliminar' or command.lower() == 'e':
        client_name = _client_name()
        if client_name != None:
            client_list = delete_client(client_name, client_list)
        list_client(client_list)
    elif command.lower() == 'actualizar' or command.lower() == 'a':
        client_name = _client_name()
        client_list = update_client(client_name, client_list)
        list_client(client_list)
        #return client_list
    elif command.lower() == 'buscar' or command.lower() == 'b':
        client_name = _client_name()
        if client_name != None:
            search_client(client_name, client_list)
    elif command.lower() == 'listar' or command.lower() == 'l':
        list_client(client_list)
    elif command.lower() == 'salir' or command.lower() == 's':
        return False
    else:
        print('>>> Comando Invalido\r\n')
        _separete()
    _continue_func()


def _client_name():
    client_name = None
    while not client_name:
        client_name = str(input('>Ingrese el nombre del cliente: '))
        if client_name == 'exit':
            client_name = None
            break
    return client_name


def _print_welcome():
    print('\t\t B I E N V E N I D O  A  P L A T Z I - V E N T A')
    _separete()

def _print_client(idx, client):
    print('\tcliente: {} >>> {} | {} | {} | {}'.format(idx,client['name'],client['compañia'],client['correo'],client['posicion']))

def _separete():
    print('*' * 80)

def _continue_func():
    contin =str(input('\n-> Presione [enter] para continuar: '))

def _adios_platzi_venta():
    os.system('clear')
    _separete()
    print('\t\t            P L A T Z I - V E N T A            ')
    _separete()

#**********************************************************************************************************************************
def main(client_list):
    while True:
        os.system('clear')
        command = _command_insert()
        if _command_select(command, client_list) == False:
            break
#**********************************************************************************************************************************

if __name__ == '__main__':
    os.system('clear')
    client_list = [
        {
            'name': 'jose',
            'compañia': 'Google',
            'correo': 'jose@oliva.com',
            'posicion': 'CEO',
        },
        {
            'name': 'martin',
            'compañia': 'facebook',
            'correo': 'martin@quiroz.com',
            'posicion': 'CTO',
        }
    ]
    main(client_list)
    _adios_platzi_venta()
