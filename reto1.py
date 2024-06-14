from datetime import *
una_fecha = '20/04/2019'
fecha_dt = datetime.strptime(una_fecha, '%d/%m/%Y')
f=fecha_dt.strftime('%x')
print(fecha_dt, f)

start_date = date(2023, 3, 1)
date_str = start_date.strftime('%d-%m-%Y')

print(date_str)