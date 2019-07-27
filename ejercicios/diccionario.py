import os
os.system('clear')

def main():
    calificaciones = dict()
    calificaciones['Algoritmos'] = 9
    calificaciones['Matematicas'] = 10
    calificaciones['Web'] = 8
    calificaciones['Bases_de_Datos'] = 10

    # a lo largo de las llaves
    for key in calificaciones:
        print(key)
    addCalificaciones = 0
    # A lo largo de los valores
    for value in calificaciones.values():
        addCalificaciones += value
        print(value)
        # Los valores no se reciben en orden
    print(addCalificaciones)
    #Iterar entre llaves y Valores en pyton 2 es iteritems()
    for key, value in calificaciones.items():
        print('> {}: {}'.format(key, value))


    promedioDeCalificaciones = (addCalificaciones/(len(calificaciones.values())))
    print('>>>El promedio de las calificaciones es: {}'.format(promedioDeCalificaciones))

if __name__ == '__main__':
    main()
