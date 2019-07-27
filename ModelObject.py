# -*- coding: utf-8 -*-
import os

class LampDeEscritorio:
    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''



         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self, is_turned_on):
        self._is_turned_on = is_turned_on
        self._display_image()
    def turn_on(self):
        self._is_turned_on = True
        self._display_image()
    def turn_off(self):
        self._is_turned_on = False
        self._display_image()
    def _display_image(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])

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
