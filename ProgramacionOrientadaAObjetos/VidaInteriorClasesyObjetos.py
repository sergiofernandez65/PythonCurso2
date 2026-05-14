class Classy:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass


obj = Classy()

#Resultado:
#{'var': 2}
#{'__module__': '__main__', 'varia': 1, '__init__': <function Classy.__init__ at 0x7ff2be459320>, 'method': <function Classy.method at 0x7ff2be459ef0>, '_Classy__hidden': <function Classy.__hidden at 0x7ff2be459f80>, '__dict__': <attribute '__dict__' of 'Classy' objects>, '__weakref__': <attribute '__weakref__' of 'Classy' objects>, '__doc__': None}


class Classy:
    pass


print(Classy.__name__)
obj = Classy()
print(type(obj).__name__)

#Resultado:
#Classy
#Classy


class Classy:
    pass


print(Classy.__module__)
obj = Classy()
print(obj.__module__)
    
#Resultado:
#__main__
#__main__


class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)
    
#Resultado:
#( object )
#( object )
#( SuperOne SuperTwo )