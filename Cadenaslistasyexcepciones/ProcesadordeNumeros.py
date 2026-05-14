#Procesador de Números.

line = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("El total es:", total)
except:
    print(substr, "no es un numero.")

#Resultado:
#Ingresa una línea de números, sepáralos con espacios: 1 2 3 4 5
#El total es: 15.0
