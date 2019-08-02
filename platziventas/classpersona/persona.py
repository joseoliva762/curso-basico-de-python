

class Persona():
    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

    def say_hello(self):
        print('Hello, my name is {}, and i am {} years old.'.format(self.name, self.age))
