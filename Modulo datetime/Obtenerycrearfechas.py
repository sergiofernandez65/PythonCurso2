from datetime import date

today = date.today()

print("Hoy:", today)
print("Año:", today.year)
print("Mes:", today.month)
print("Día:", today.day)

#Resultado
# Hoy: 2026-05-12
#Año: 2026
#Mes: 5
#Día: 12
   

from datetime import date

my_date = date(2019, 11, 4)
print(my_date)
    
#Resultado:
#2019-11-04


from datetime import date
import time

timestamp = time.time()
print("Marca de tiempo:", timestamp)

d = date.fromtimestamp(timestamp)
print("Fecha:", d)
    
#Resultado
#Marca de tiempo: 1778582222.2726738
#Fecha: 2026-05-12