'''
Listas

Una lista es una conleccion ordenada y mutable(se puede modificar) y
pueden almacenar elementos de cualquier tipo.

Caracteristicas:
* Son ordenadas 
* Son mutables
* Pueden contener elementos duplicados
* Los elementos puede ser de diferentes tipo de datos 
'''
#Definicion de una lista 
mi_lista = [10, 20 ,30 ,40, "Hola"]
print(mi_lista)

#Acceder a un elemento
print(mi_lista[3]) #Salida: 40

#Modificar un elemento
mi_lista[3] = "Adios"
print(mi_lista) #Salida: [10, 20, 30, 'Adios', 'Hola']

#Agregar un elemento 
mi_lista.append(50)
print(mi_lista) #Salida: [10, 20, 30, 'Adios', 'Hola', 50]

#Eliminar un elemento
# mi_lista.remove(mi_lista[0]) # Opcion 1 Pos
mi_lista.remove(10)  #  Opcion 2 busqueda
print(mi_lista) #Salida: [20, 30, 'Adios', 'Hola', 50]

#longitud de la lista
print(len(mi_lista))

'''
Operadores 
* append(): Agrega un elemento al final
* remove(): Elimina el primer elemento que coincide con el valor
* len(): Devuelve la longitud de la lista
'''
lista = [1,"Hola", True]

lista = [1,"Hola", True, lista]

print(lista)