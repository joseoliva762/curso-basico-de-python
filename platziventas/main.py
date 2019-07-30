
def create_client(client_name, client_list):
    if client_name not in client_list:
        client_list = _add_coma(client_list)
        client_list += client_name
    else:
        print('\nEl cliente ya esta en la lista.\n')
    return client_list

def update_client(client_list):
    client_name = _client_name()
    updated_name = str(input('>Cual es el nuevo nombre: '))
    if client_name in client_list:
        client_list = client_list.replace(client_name ,updated_name)
        return client_list
    else:
        print('Client not in client\'s list')

def _command_insert():
    _print_welcome()
    return str(input('Que quiere hacer hoy?\n\t >[crear]      cliente.\n\t >[borrar]     cliente.\n\t >[actualizar] cliente.\n Opcion: '))

def _command_select(command, client_list):
    if command.lower() == 'crear' or command.lower() == 'c':
        client_name = _client_name()
        client_list = create_client(client_name, client_list)
        _print_list(client_list)
    elif command.lower() == 'borrar' or command.lower() == 'b':
        pass
    elif command.lower() == 'actualizar' or command.lower() == 'a':
        client_list = update_client(client_list)
        _print_list(client_list)
        return client_list
    else:
        print('\tComando Invalido\r\n')

def _client_name():
    return str(input('>Ingrese el nombre del cliente: '))

def _print_list(client_list):
    print(client_list)

def _add_coma(clients_list):
    return clients_list + ', '

def _print_welcome():
    print(' B I E N V E N I D O  A  P L A T Z I - V E N T A')
    print('*' * 50)

def main(client_list):
    command = _command_insert()
    _command_select(command, client_list)

if __name__ == '__main__':
    client_list = 'jose, martin'
    main(client_list)
