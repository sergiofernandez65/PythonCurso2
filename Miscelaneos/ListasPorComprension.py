list_1 = []

for ex in range(6):
    list_1.append(10 ** ex)

list_2 = [10 ** ex for ex in range(6)]

print(list_1)
print(list_2)
    
#Resultado:
#[1, 10, 100, 1000, 10000, 100000]
#[1, 10, 100, 1000, 10000, 100000]


the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list)

#Resultado:
#[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]


the_list = [1 if x % 2 == 0 else 0 for x in range(10)]

print(the_list)

#Resultado:
#[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]