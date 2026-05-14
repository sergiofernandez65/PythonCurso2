class Top:
    def m_top(self):
        print("superior")


class Middle(Top):
    def m_middle(self):
        print("Medio")


class Bottom(Middle):
    def m_bottom(self):
        print("abajo")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

#Resultado:
#abajo
#Medio
#superior


class Top:
    def m_top(self):
        print("superior")


class Middle(Top):
    def m_middle(self):
        print("medio")


class Bottom(Middle, Top):
    def m_bottom(self):
        print("abajo")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()
    
#Resultado:
#abajo
#medio
#superior


class Top:
    def m_top(self):
        print("superior")


class Middle(Top):
    def m_middle(self):
        print("medio")


class Bottom(Top, Middle):
    def m_bottom(self):
        print("abajo")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()
    
#Resultado:
#Traceback (most recent call last):
#  File "main.py", line 11, in <module>
#    class Bottom(Top, Middle):
#TypeError: Cannot create a consistent method resolution
#order (MRO) for bases Top, Middle