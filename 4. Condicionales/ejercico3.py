'''Escribe un programa que pida una calificación numérica (0-100) y determine si 
el estudiante aprueba o no (60 o más es aprobado)'''
import math

calificacion = float(input("Ingrese tu calificacion: "))

calificacion = round(calificacion) #Redondeo general 
#calificacion = math.floor(calificacion) #Redondeo hacia bajo 
#calificacion = math.ceil(calificacion) #Redondeo hacia Arriba 

print(calificacion)

if calificacion >= 60 and calificacion <=100:
    print("Aprobo")
elif calificacion >= 0 and calificacion <60:
    print("Reprobo")
else:
    print("La calificacion no es valida")