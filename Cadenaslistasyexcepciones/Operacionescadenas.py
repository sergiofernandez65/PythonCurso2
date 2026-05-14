str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

#Resultado:
#ab
#ba
#aaaaa
#bbbb


# Demostración de la función ord().

char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))

#Resultado:
#97
#32


# Demostración de la función chr().

print(chr(97))
print(chr(945))

#Resultado:
#a
#α


# Demonstración de min() - Ejemplo 1:
print(min("aAbByYzZ"))


# Demonstración de min() - Ejemplos 2 y 3:
t = 'Los Caballeros Que Dicen "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

#Resultado:
#A
#[ ]
#0


# Demostración de max() - Ejemplo 1:
print(max("aAbByYzZ"))


# Demostración de max() - Ejemplo 2 y 3:
t = 'Los Caballeros Que Dicen "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

#Resultado:
#z
#[u]
#2

# Demonstración del método index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

#Resultado:
#2
#7
#1


# Demostración de la función list():
print(list("abcabc"))

#Resultado:
#['a', 'b', 'c', 'a', 'b', 'c']


# Demostración del método count():
print("abcabc".count("b"))
print('abcabc'.count("d"))

#Resultado:
#2
#0