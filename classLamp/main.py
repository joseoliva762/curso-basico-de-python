import os
from classLamp import LampDeEscritorio

def resive_command():
    return str(input('Que desea hacer: \n\t> [P]render.\n\t> [A]pagar.\n\t> [S]alir \n>Opcion: ')).lower()

def lampDesk_state(command, lamp):
    while True:
        if command == 'p':
            os.system('clear')
            lamp.turn_on()
            return command
        elif command == 'a':
            os.system('clear')
            lamp.turn_off()
            return command
        elif command == 's':
            os.system('clear')
            return command
        else:
            os.system('clear')
            print('>>>Escoja una opcion correcta.\n\n\n\n\n\n\n\n\n')
            command = resive_command()

def main():
    #instanciamos una lampara.
    lamp = LampDeEscritorio(is_turned_on = True)
    while True:
        command = lampDesk_state(resive_command(),lamp)
        if command == 's':
            break

if __name__ == '__main__':
    os.system('clear')
    main()
