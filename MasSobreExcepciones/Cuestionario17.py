Pregunta 1: ¿Cuál es el resultado esperado del siguiente código?

import math
 
    try:
        print(math.sqrt(9))
    except ValueError:
        print("inf")
    else:
        print("ok")
 
3.0
ok


Pregunta 2: ¿Cuál es el resultado esperado del siguiente código?

import math
 
    try:
        print(math.sqrt(-9))
    except ValueError:
        print("inf")
    else:
        print("ok")
    finally:
        print("fin")
 
inf
fin


Pregunta 3: ¿Cuál es el resultado esperado del siguiente código?

import math
 
class NewValueError(ValueError):
    def __init__(self, name, color, state):
        self.data = (name, color, state)
 
try:
    raise NewValueError("Advertencia enemiga", "Alerta roja", "Alta disponibilidad")
except NewValueError as nve:
    for arg in nve.args:
        print(arg, end='! ')
 
Advertencia enemiga! Alerta roja! Alta disponibilidad!