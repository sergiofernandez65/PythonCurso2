from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)

#Resultado:
#True
#True
#True
#True



from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))

#Resultado:
#False
#True
#True


from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))

#Resultado:
#1 2
# -2 -3
#2 3
# -1 -2
#1 2
# -1 -2


from random import random

for i in range(5):
    print(random())

#Resultado: 5 números aleatorios entre 0 y 1


from random import random, seed

seed(0)

for i in range(5):
    print(random())

#Resultado: 5 números aleatorios entre 0 y 1, pero siempre los mismos


from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

#Resultado:
#0 0 0 0


from random import randint

for i in range(10):
    print(randint(1, 10), end=',')

#Resultado: 10 números aleatorios entre 1 y 10, ambos incluidos


from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

#Resultado:
#1
#[6, 10, 5, 3, 9]
#[9, 1, 3, 10, 7, 4, 6, 2, 8, 5]


platform(aliased = False, terse = False)


from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))


from platform import machine

print(machine())


from platform import processor

print(processor())



from platform import system

print(system())


from platform import version

print(version())


from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)

#Resultado:
#CPython
#3
#10
#4
