# -*- coding: utf-8 -*-
import os

def busquedaBinaria(numeros, inNumero, minIdx, maxIdx):
    if minIdx > maxIdx:
        return False
    midIdx = int((minIdx + maxIdx) / 2)
    if numeros[midIdx] == inNumero:
        return True
    elif numeros[midIdx] > inNumero:
        return busquedaBinaria(numeros, inNumero, minIdx, midIdx-1)
    else:
        return busquedaBinaria(numeros, inNumero, midIdx + 1, maxIdx)


def main():
    numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,50,75,100]
    inNumero = int(input('>> Ingresa un numero: '))
    findNumero = busquedaBinaria(numeros, inNumero, 0, len(numeros)-1)
    if findNumero == True:
        print('El numero {}, si está en la lista.'.format(inNumero))
    else:
        print('El número {}, no está en la lista.'. format(inNumero))

if __name__ == '__main__':
    os.system('clear')
    main()
