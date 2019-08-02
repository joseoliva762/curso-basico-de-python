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
    return True


def upper(func):
    def wrapper(*args, **kwards):
        if _needs_password():
            return func(name_user = args[0].upper())
    return wrapper

@upper
def say_my_name(nombre):
    return 'Hola, {} Bienvenido a Platzi Ventas'.format(nombre)

def main():
    print(say_my_name(str(input('>User: '))))

if __name__ == '__main__':
    main()
