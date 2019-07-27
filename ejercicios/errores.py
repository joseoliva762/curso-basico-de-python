# -*- coding: utf-8 -*-
COUNTRIES = {
    'mexico' : 122,
    'colombia' : 49,
    'argentina' : 43,
    'chile' : 18,
    'peru' : 31
}

def main():
    while True:
        country = str(input('Nombre del Pais: ')).lower() #para optener siempre la llave en minusculas.
        try:
            print('\tLa poblacion de {}, es de {} Millones.'.format(country, COUNTRIES[country]))
        except KeyError:
            print('No tenemos el Dato de la poblacion de {}.'.format(country))


if __name__ == '__main__':
    main()
