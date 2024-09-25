'''
Tuplas

Una tupla es una coleccion ordenada pero inmutable, lo que significa que no
se puede modificar los elementos una ves definidos.

Caracteristicas:
* Son ordenadas 
* Son inmutables
* Pueden contener elementos duplicados
* Los elementos puede ser de diferentes tipo de datos 
'''
#Definicion de una tupla
mi_tupla = (10, 20 ,30 ,40, "Hola")

#Acceder a un elemento
print(mi_tupla[2]) #Salida: 30

#Intentar modificar un elemento
# mi_tupla[1] = 40 #Esto genera un error: TypeError

# Longitud de la tupla
print(len(mi_tupla))

'''
Operadores 
* len(): Devuelve la longitud de la lista
'''