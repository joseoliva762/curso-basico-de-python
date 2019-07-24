
def palindrome(palabra):
    reverse_letter = []
    for letter in palabra:
        reverse_letter.insert(0, letter)
    reverseWord = ''.join(reverse_letter)
    if reverseWord == palabra:
        return True
    else:
        return False

def main():
    sussecs = False
    palabra = str(input('Ingrese una palabra: '))
    sussecs = palindrome(palabra)

    if sussecs == True:
        es = ' '
    else:
        es = ' No '

    print('La palabra {},{}es un palindomo.'.format(palabra, es))


if __name__ == '__main__':
    while True:
        main()
