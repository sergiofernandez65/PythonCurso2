from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print(delta)

#Resultado:
#16 days, 3:00:00



from datetime import timedelta
from datetime import date
from datetime import datetime

delta = timedelta(weeks=2, days=2, hours=2)
print(delta)

delta2 = delta * 2
print(delta2)

d = date(2019, 10, 4) + delta2
print(d)

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)

#Resultado:
#16 days, 2:00:00
#32 days, 4:00:00
#2019-11-05
#2019-11-05 18:53:00