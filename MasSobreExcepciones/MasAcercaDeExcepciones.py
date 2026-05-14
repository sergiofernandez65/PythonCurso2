def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("División fallida")
        return None
    else:
        print("Todo salió bien")
        return n


print(reciprocal(2))
print(reciprocal(0))
    
#Resultado:
#Todo salió bien
#0.5
#División fallida
#None


def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("División fallida")
        n = None
    else:
        print("Todo salió bien")
    finally:
        print("Es momento de decir adiós")
        return n


print(reciprocal(2))
print(reciprocal(0))
    
#Resultado:
#Todo salió bien
#Es momento de decir adiós
#0.5
#División fallida
#Es momento de decir adiós
#None