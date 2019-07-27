# -*- coding: utf-8 -*-
def protected(func):
    def wrapper(password):
        if password == 'Platzi':
            return func()
        else:
            print('\n\t>>la contraseña es incorrecta.\r\n')
    return wrapper

@protected
def protected_func():
    print('\n\t>>Tu contraseña es correcta.\r\n')

def password_recive():
    return str(input('>>Escribe la contraseña: '))

def main():
    password = password_recive()
    #wrapper = protected(protected_func)
    #wapper(password)

    protected_func(password)

if __name__ == '__main__':
    main()
