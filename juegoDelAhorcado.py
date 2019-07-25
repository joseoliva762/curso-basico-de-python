import random
import os
IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']
PALABRAS = ['lavadora', 'secadora', 'sofa', 'gobierno','diputado','democracia','computador','teclado', 'jose']

def randomWord():
    idxWord = random.randint(0,len(PALABRAS)-1)
    return PALABRAS[idxWord]

def showBoard(hiddenWord, tries):
    print('\tA H O R C A D O S\r\n')
    print(IMAGES[tries])
    print(' ')
    print(hiddenWord)
    print('---- * ---- * ---- * ---- * ---- * ---- * ---- * ---- * ----')

def selectLetter(passSelectLetter):
    cont = 0
    while True:
        if cont == 0:
            letter = str(input('>>> Escoge una letra: '))
        else:
            letter = str(input('>>> Ya haz escogido esa letra, Escoge una nueva letra: '))
        try:
            passSelectLetter.index(letter)
            cont += 1
        except ValueError:
            passSelectLetter.append(letter)
            break
    return letter


def main():
    passSelectLetter = []
    word = randomWord()
    hiddenWord = ['_'] * len(word)
    tries = 0
    os.system ("clear")
    while(True):
        showBoard(hiddenWord, tries)
        letter = selectLetter(passSelectLetter)
        idxLetter = list()
        for idx in range(len(word)):
            if word[idx] == letter:
                idxLetter.append(idx)
        if len(idxLetter) == 0:
            tries += 1
        else:
            for idx in idxLetter:
                hiddenWord[idx] = letter
            idxLetter = []
        os.system ("clear")
        #para windows os.system ("cls")
        if tries == 7:
            showBoard(hiddenWord, tries)
            print('\tPerdiste!!, la palabro oculta era: {}.'.format(word))
            break

        #la funcion index nos pregunta si encontro algo en una lista
        #manejo de errores con try:
        try:
            hiddenWord.index('_')
        except ValueError:
            showBoard(hiddenWord, tries)
            print('\tFelicidades!!! Ganaste, la parabra es: {}.'.format(word))
            break


if __name__ == '__main__':
    while True:
        main()
        keepPlaying = str(input('\r\nQuieres seguir jugando? [si/no]: '))
        while keepPlaying != 'si' and keepPlaying != 'no':
                keepPlaying = str(input('Elija una opcion correcta [si/no]: '))
        if keepPlaying == 'no':
            break
