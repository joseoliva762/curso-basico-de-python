def conversor(ammount):
    MEX_TO_COP =145.97
    return ammount * MEX_TO_COP

def main():
    print('\t>>>Calculadora de divisas<<<\r\n')
    print('Convierte de pesos Mexicanos a pesos Colombianos.\r\n')

    ammount = float(input('Valor en pesos Mexicanos: '))
    COP = conversor(ammount)
    print('${} Pesos mexicanos son: \r\n\t ${} COP'.format(ammount,COP))

if __name__=='__main__':
    main()
