def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)
    
#Resultado
#f(-2)=18
#f(-1)=8
#f(0)=2
#f(1)=0
#f(2)=2


list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()
    
#Resultado:
#[1, 2, 4, 8, 16]
#1 4 16 64 256 


from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)

#Resultado:
#[-9, -3, 6, -9, -6]
#[6]