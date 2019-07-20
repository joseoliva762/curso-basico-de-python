def isPrime(numero):
    if numero < 2:
        return False
    elif numero == 2:
        return True
    elif numero > 2 and numero%2  == 0:
        return False
    else:
        for cont in range(3, numero):
            if numero%cont == 0:
                return False
        return True



def main():
    numero = int(input('Escribe un numero: '))
    result = isPrime(numero)
    if result == True:
        strResult = ' '
    else:
        strResult = ' No '
    print('El numero {},{}es Primo.\r\n'.format(numero, strResult))

if __name__=='__main__':
    main()
