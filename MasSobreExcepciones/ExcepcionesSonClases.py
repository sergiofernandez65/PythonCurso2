try:
    i = int("¡Hola!")
except Exception as e:
    print(e)
    print(e.__str__())
    
#Resultado:
#invalid literal for int() with base 10: '¡Hola!'
#invalid literal for int() with base 10: '¡Hola!'


def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)


print_exception_tree(BaseException)
    
#Resultado:
#BaseException
#   +---Exception
#       +---ArithmeticError
#           +---FloatingPointError
#           +---OverflowError
#           +---ZeroDivisionError
#       +---AssertionError
#       +---AttributeError
#       +---BufferError
#       +---EOFError
#       +---ImportError
#       +---LookupError
#           +---IndexError
#           +---KeyError
#       +---MemoryError
#       +---NameError
#       +---OSError
#       +---ReferenceError
#       +---RuntimeError
#           +---NotImplementedError
#       +---StopIteration
#       +---SyntaxError
#       +---SystemError
#       +---TypeError
#       +---ValueError
