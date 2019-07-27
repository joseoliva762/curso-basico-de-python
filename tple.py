"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""

def first_not_repeating_char(char_sequence):
    seen_letter = dict()
    for idx, letter in enumerate(char_sequence):
        if letter not in seen_letter:
            seen_letter[letter] = (idx, 1)
        else:
            seen_letter[letter] = (seen_letter[letter][0], seen_letter[letter][1] + 1)
    final_letter = []
    for key, value in seen_letter.items():
            if value[1] == 1:
                final_letter.append((key,value[0]))
    not_repited_letter = sorted(final_letter, key=lambda value: value[1])

    if not_repited_letter:
        return not_repited_letter[0][0]
    return '_'


if __name__ == '__main__':
    char_sequence = str(input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print('El primer caracter no repetido es: {}'.format(result))
