Pregunta 1: ¿Cuál es el resultado esperado del siguiente código?

class Vowels:
    def __init__(self):
        self.vow = "aeiouy " # Sí, sabemos que y no siempre se considera una vocal.
        self.pos = 0
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.pos == len(self.vow):
            raise StopIteration
        self.pos += 1
        return self.vow[self.pos - 1]
 
 
vowels = Vowels()
for v in vowels:
    print(v, end=' ')
 
a e i o u y


Pregunta 2: Escribe una función lambda, estableciendo a 1 su argumento entero, y aplícalo a la función map() para producir la cadena 1 3 3 5 en la consola.

any_list = [1, 2, 3, 4]
even_list = # Completa la línea aquí.
print(even_list)
 
list(map(lambda n: n | 1, any_list))
    

Pregunta 3: ¿Cuál es el resultado esperado del siguiente código?

def replace_spaces(replacement='*'):
    def new_replacement(text):
        return text.replace(' ', replacement)
    return new_replacement
 
 
stars = replace_spaces()
print(stars("And Now for Something Completely Different"))
 
And*Now*for*Something*Completely*Different