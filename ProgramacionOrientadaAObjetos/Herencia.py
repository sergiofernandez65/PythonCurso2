class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy


sun = Star("Sol", "Vía Láctea")
print(sun)

#Resultado:
#<__main__.Star object at 0x000001B9F8C1E5B0>


<code>class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return self.name + ' en ' + self.galaxy


sun = Star("Sol", "Vía Láctea")
print(sun)

#Resultado:
#File "main.py", line 2
#   <code>class Star:
#    ^
#SyntaxError: invalid syntax


class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass

