class Classy:
    def method(self):
        print("método")


obj = Classy()
obj.method()

#Resultado:
#método


class Classy:
    def __init__(self, value):
        self.var = value


obj_1 = Classy("objeto")

print(obj_1.var)

#Resultado:
#objeto


class Classy:
    def __init__(self, value = None):
        self.var = value


obj_1 = Classy("objeto")
obj_2 = Classy()

print(obj_1.var)
print(obj_2.var)
    
#Resultado:
#objeto
#None