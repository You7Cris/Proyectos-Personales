# almacenar hora y fecha

from datetime import datetime
from datetime import date
import datetime

mi_hora = datetime.time(17, 56)

mi_dia = datetime.date(2025, 10, 17)

mi_fecha = datetime(2025, 5, 15, 22, 10, 15, 2500)

mi_fecha = mi_fecha.replace(month=6)

print(mi_dia.ctime())

print(mi_dia.today())

print(mi_hora)
print(type(mi_hora))

nacimiento = date(1995, 3, 5)
defuncion = date(2095, 6, 19)

vida = defuncion - nacimiento

print(vida.days)

despierta = datetime(2022, 10, 5, 7, 30)
duerme = datetime(2022, 10, 5, 23, 45)

vigilia = duerme - despierta

print(vigilia.seconds)
