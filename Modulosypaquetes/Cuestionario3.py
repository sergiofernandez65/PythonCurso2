Pregunta 1: Deseas evitar que el usuario de tu módulo ejecute tu código como un script ordinario. ¿Cómo lograrías tal efecto?

import sys

if __name__ == "__main__":
    print "Don't do that!"
    sys.exit()


Pregunta 2: Algunos paquetes adicionales y necesarios se almacenan dentro del directorio D:\Python\Project\Modules directory. Escribe un código asegurándote de que Python recorra el directorio para encontrar todos los módulos solicitados.

import sys

# ¡Toma en cuenta las diagonales invertidas dobles!
sys.path.append("D:\\Python\\Project\\Modules")


Pregunta 3: El directorio mencionado en el Pregunta anterior contiene un subárbol con la siguiente estructura:

abc
 |__ def
     |__ mymodule.py
Asumiendo que D:\Python\Project\Modules se ha adjuntado con éxito a la lista sys.path, escribe una directiva de importación que te permita usar todas las entidades de mymodule.

import abc.def.mymodule