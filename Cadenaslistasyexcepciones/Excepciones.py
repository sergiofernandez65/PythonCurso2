value = 1
value /= 0

#Resultado:
#Traceback (most recent call last):
#  File "Excepciones.py", line 3, in <module>
#    value /= 0
#ZeroDivisionError: division by zero


my_list = []
x = my_list[0]

#Resultado:
#Traceback (most recent call last):
#  File "Excepciones.py", line 8, in <module>
#    x = my_list[0]
#IndexError: list index out of range


first_number = int(input("Ingresa el primer número: "))
second_number = int(input("Ingresa el segundo número: "))

if second_number != 0:
    print(first_number / second_number)
else:
    print("Esta operación no puede ser realizada.")

print("FIN.")

#Resultado:
#Ingresa el primer número: 10
#Ingresa el segundo número: 0
#Esta operación no puede ser realizada.
#FIN.


first_number = int(input("Ingresa el primer número: "))
second_number = int(input("Ingresa el segundo numero: "))

try:
    print(first_number / second_number)
except:
    print("Esta operación no puede ser realizada.")

print("FIN.")

#Resultado:
#Ingresa el primer número: 10
#Ingresa el segundo numero: 0
#Esta operación no puede ser realizada.
#FIN.


try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh cielos, algo salió mal...")

print("3")
    
#Resultado:
#1
#Oh cielos, algo salió mal...
#3


try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
except:
    print("Oh cielos, algo salió mal...")

print("FIN.")

#Resultado:
#Ingresa un numero: 0
#Oh cielos, algo salió mal...
#FIN.


try:
    x = int(input("Ingresa un número: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
except ValueError:
    print("Debes ingresar un valor entero..")
except:
    print("Oh cielos, algo salió mal...")

print("FIN.")

#Resultado:
#Ingresa un número: 0
#No puedes dividir entre cero, lo siento.
#FIN.


try:
    x = int(input("Ingresa un número: "))
    y = 1 / x
    print(y)
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Oh cielos, algo salió mal...")

print("FIN.")

#Resultado:
#Ingresa un número: hola
#Debes ingresar un valor entero.
#FIN.


try:
    x = int(input("Ingresa un número: "))
    y = 1 / x
    print(y)
except ValueError:
    print("Debes ingresar un valor entero.")

print("FIN.")

#Resultado:
#Ingresa un número: hola
#Debes ingresar un valor entero.
#FIN.


try:
    y = 1 / 0
except ZeroDivisionError:
    print("Uuupsss...")

print("FIN.")

#Resultado:
#Uuupsss...
#FIN.


try:
    y = 1 / 0
except ZeroDivisionError:
    print("¡División entre cero!")
except ArithmeticError:
    print("¡Problema Aritmético!")

print("FIN.")

#Resultado:
#¡División entre cero!
#FIN.


def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("¡Problema aritmético!")
    return None

bad_fun(0)

print("FIN.")

#Resultado:
#¡Problema aritmético!
#FIN.


def bad_fun(n):
    raise ZeroDivisionError


try:
    bad_fun(0)
except ArithmeticError:
    print("¿Qué pasó? ¿Un error?")

print("FIN.")

#Resultado:
#¿Qué pasó? ¿Un error?
#FIN.


def bad_fun(n):
    try:
        return n / 0
    except:
        print("¡Lo hice otra vez!")
        raise


try:
    bad_fun(0)
except ArithmeticError:
    print("¡Ya veo!")

print("FIN.")

#Resultado:
#¡Lo hice otra vez!
#¡Ya veo!
#FIN.


import math

x = float(input("Ingresa un número: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)

#Resultado:
#Ingresa un número: -1
#Traceback (most recent call last):
#  File "Excepciones.py", line 122, in <module>
#    assert x >= 0.0
#AssertionError




# El codigo muestra una forma extravagante
# de dejar el bucle.

the_list = [1, 2, 3, 4, 5]
ix = 0
do_it = True

while do_it:
    try:
        print(the_list[ix])
        ix += 1
    except IndexError:
        do_it = False

print('Listo')



# Este código no puede ser abortado
# presionando Ctrl-C.

from time import sleep

seconds = 0

while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("¡No hagas eso!")



# Este código causa la excepción MemoryError.
# Advertencia: el ejecutar este código puede afectar tu Sistema Operativo.
# ¡No lo ejecutes en entornos de producción!

string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print('¡Esto no es gracioso!')



# El código imprime los valores subsequentes
# de exp(k), k = 1, 2, 4, 8, 16, ...

from math import exp

ex = 1

try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('El número es demasiado grande.')



># Una de estas importaciones fallará, ¿cuál será?

try:
    import math
    import time
    import abracadabra:

except:
    print('Una de tus importaciones ha fallado.')



# ¿Cómo abusar del diccionario
# y cómo lidiar con ello?

dictionary = {'a': 'b', 'b': 'c', 'c': 'd'}
ch = 'a'

try:
    while True:
        ch = dictionary[ch]
        print(ch)
except KeyError:
    print('No existe tal clave:', ch)



