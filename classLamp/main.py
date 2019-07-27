def resive_command():
    return str(input('Que desea hacer: \n\t> [P]render.\n\t> [A]pagar.\n\t> [S]alir \n>Opcion: ')).lower()

def main():
    #instanciamos una lampara.
    lamp = LampDeEscritorio(is_turned_on = True)
    while True:
        command = resive_command()
        if command == 'p':
            os.system('clear')
            lamp.turn_on()
        elif command == 'a':
            os.system('clear')
            lamp.turn_off()
        elif command == 's':
            os.system('clear')
            break
        else:
            os.system('clear')
            print('>>>Escoja una opcion correcta.\r\n')

if __name__ == '__main__':
    os.system('clear')
    main()
