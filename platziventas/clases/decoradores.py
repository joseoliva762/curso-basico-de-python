PASSWORD = '12345'

def password_required(func):
    def wrapper():
        password = str(input('>>Contraseña requerida: '))
        if password == PASSWORD:
            return func()
        else:
            print('\tContraseña incorrecta.')
    return wrapper

@password_required
def _needs_password():
    print('\tLa contraseña es correcta!!')


def main():
    _needs_password()

if __name__ == '__main__':
    main()
