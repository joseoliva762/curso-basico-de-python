# -*- coding: utf-8 -*-
def factorial(inNumber):
    if inNumber == 0:
        return 1
    else:
        return inNumber * factorial(inNumber - 1)

def main():
    inNumber = int(input('Escriba el numero: '))
    result = factorial(inNumber)
    print('el resultado de {}! es: {}'.format(inNumber,result))


if __name__ == '__main__':
    main()
