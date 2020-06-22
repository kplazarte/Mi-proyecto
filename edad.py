# Codigo de ejemplo para Git
# Autor: Kevin Plazarte <kplazarte@est.ups.edu.ec>
# Fecha: 22-06-2020
# Version 0.0.1
# Calcular la edad del año actual
anio = 2020
mes_actual = 6
nombre = input("Cual es tu nombre? ")
anio_nacimiento = int(input("En que año naciste: "))
mes_nacimiento = int (input("En que mes naciste: "))
edad = anio - anio_nacimiento
if mes_nacimiento > mes_actual:
	edad -= 1
print("\nHola" , nombre , "tu edad en este año es:", edad); 
