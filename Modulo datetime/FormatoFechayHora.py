from datetime import date

d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))

#2020/01/04


from datetime import time
from datetime import datetime

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))

#Resultado:
#14:53:00
#20/November/04 14:53:00