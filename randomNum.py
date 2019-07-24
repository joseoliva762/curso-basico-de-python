# -*- coding:utf-8 -*-
import random

def main():
    numberFound = False
    maxNumber = int(input('Ingrese el numero maximo de posibilidades: '))
    randomNumber = random.randint(0,maxNumber)

    while not numberFound: #mientras no encontramos el numero.
        number = int(input("Ingresa un numero: "))
        if number == randomNumber:
            print('\tFelicidades!!! encontraste el numero. El numero  es: {}\r\n'.format(randomNumber))
            numberFound = True
        elif number > randomNumber:
            print('\r\n>>> El numero es mas pequeno.\n')
        elif number < randomNumber:
            print('\r\n>>> El numero es mas grande. \n')
        else:
            continue

if __name__ == '__main__':
    main()
