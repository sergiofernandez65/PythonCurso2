Escenario
Supongamos que el siguiente fragmento de código se ha ejecutado con éxito:


class Dog:
    kennel = 0
    def __init__(self, breed):
        self.breed = breed
        Dog.kennel += 1
    def __str__(self):
        return self.breed + " says: ¡Guau!"
 
 
class SheepDog(Dog):
    def __str__(self):
        return super().__str__() + " ¡No huyas, Corderito!"
 
 
class GuardDog(Dog):
    def __str__(self):
        return super().__str__() + " ¡Quédese donde está, Señor Intruso!"
 
 
rocky = SheepDog("Collie")
luna = GuardDog("Dobermann")
 

Ahora responde las preguntas 1-4.


Pregunta 1: La declaración de la clase Snake se da a continuación. Enriquece la clase con un método llamado increment(), que aumente en 1 a la propiedad __victims.

print(rocky)
print(luna)
 
Collie dice: ¡Guau! ¡No huyas, Corderito!
Dobermann dice: ¡Guau! ¡Quédese donde está, Señor Intruso!


Pregunta 2: ¿Cuál es el resultado esperado del siguiente código?

print(issubclass(SheepDog, Dog), issubclass(SheepDog, GuardDog))
print(isinstance(rocky, GuardDog), isinstance(luna, GuardDog))
 
True False
False True


Pregunta 3: ¿Cuál es el resultado esperado de la siguiente pieza de código?

print(luna is luna, rocky is luna)
print(rocky.kennel)
 
True False
2


Pregunta 4: Define una subclase de SheepDog llamada LowlandDog, y equipala con un método __str__() que anule un método heredado del mismo nombre. El nuevo método __str__() debe retornar la cadena "¡Guau! ¡No me gustan las montañas!".

class LowlandDog(SheepDog):
	def __str__(self):
		return Dog.__str__(self) + " ¡No me gustan las montañas!"