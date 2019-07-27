# -*- coding: utf-8 -*-
import os

KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}


def showDisplay(control):
    os.system('clear')
    if control == 0:
        print('\tC R Y P T\r\n')
    else:
        print('Escoge una opcion correcta por favor.\r\n')

    command = str(input('>> Que desea hacer? \n\t[c]ifrar el mensaje.\n\t[d]ecifrar el mensaje.\n\t[s]alir.\nOpcion: '))

    return command

def cryptMessege(messege):
    words = messege.split(' ')
    cryptMessege = []
    for word in words:
        cryptWord = ''
        for letter in word:
            cryptWord += KEYS[letter]
        cryptMessege.append(cryptWord)
    return ' '.join(cryptMessege)

def showCryptMessege(command, crypt):
    while True:
        if command == 'c':
            print('Mensaje encriptado: {}\r\n'.format(crypt))
        if (str(input('>Presione [si] para continuar: '))) == 'si':
            break

def deCryptMessege(messege):
    words = messege.split(' ')
    decryptMessege = []
    for word in words:
        decryptWord = ''
        for letter in word:
            for key, value in KEYS.items():
                if value == letter:
                    decryptWord += key
        decryptMessege.append(decryptWord)
    return ''.join(decryptMessege)

def showDecryptMessege(command, decrypt):
    while True:
        if command == 'd':
            print('Mensaje desencriptado: {}\r\n'.format(decrypt))
        if (str(input('>Presione [si] para continuar: '))) == 'si':
            break

def main():
    control = 0

    while True:
        command = showDisplay(control)
        if command == 'c':
            messege = str(input('Por favor, Escribe tu mensaje: '))
            crypt = cryptMessege(messege)
            showCryptMessege(command, crypt)
            control = 0
        elif command == 'd':
            messege = str(input('Por favor, Escribe tu mensaje encriptado: '))
            decrypt = deCryptMessege(messege)
            showDecryptMessege(command, decrypt)
            control = 0
        elif command == 's':
            break
        else:
            control = 1



if __name__ == '__main__':
    os.system('clear')
    main()
