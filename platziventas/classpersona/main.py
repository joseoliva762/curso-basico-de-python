from persona import Persona

def main():
    persona = Persona('jose', '21')

    persona.say_hello()

    persona.name = 'Jose Oliva'

    persona.say_hello()

if __name__ == '__main__':
    main()
