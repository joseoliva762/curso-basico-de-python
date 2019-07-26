"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""
def exist(repet_in_text, letter_in_text):
    nonExist = True
    for cont in range(len(repet_in_text)):
        if repet_in_text[cont] == 1:
            nonExist = False
            break
        else:
            continue
    if nonExist == False:
        return letter_in_text[cont]
    else:
        return '_'

def first_not_repeating_char(char_sequence):
    if char_sequence == 'exit':
        return 'exit'
    letter_in_text = list()
    repet_in_text = list()
    for letter in char_sequence:
        if letter != ' ':
            repet = 0
            try:
                letter_in_text.index(letter)
            except ValueError:
                letter_in_text.append(letter)
                for verifyLetter in char_sequence:
                    if verifyLetter == letter:
                        repet += 1
                repet_in_text.append(repet)
    ##print(letter_in_text)
    ##print(repet_in_text)
    return exist(repet_in_text, letter_in_text)


def main():
    char_sequence = str(input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten.')
    elif result == 'exit':
        return 'exit'
    else:
        print('El primer caracter no repetido es: {}'.format(result))

if __name__ == '__main__':
    while True:
        exit = main()
        if exit == 'exit':
            break
        else: continue
