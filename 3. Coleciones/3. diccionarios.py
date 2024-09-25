'''
Diccionarios 

Un diccionario es una coleccion desaronada de pares Clavo-Valor, donde cada clasve es unica
y estar acociada a un valor. se utiliza para representar realciones de datos, como una tabla

Caracteristicas:

* Los elementos se almacenan como pares clave-valor
* Son mutables
* Las claves son unicas, pero los valores pueden repetirse
* las claves debe ser inmutables
'''

#Definicion de un diccionario
mi_diccionario = {
    "nombre":   "Juan David",
    "edad":     28,
    "ciudad":   "Ibague",
    "idiomas":  ["ingles","español","frances"],
    "GrupoSanginio": None
}
print(mi_diccionario)

#Acceder a un valor mediante su clave
print(mi_diccionario["nombre"]) #Salida: Juan David

#Modificar un valor
mi_diccionario["edad"] = 27
print(mi_diccionario) # {'nombre': 'Juan David', 'edad': 27, 'ciudad': 'Ibague'}

#Agregar un nuevo par de clave-valor
mi_diccionario["profesion"] = "Ingeniero"
print(mi_diccionario)

#Eliminar un par de clave-valor
del mi_diccionario["ciudad"]
print(mi_diccionario)

'''
Operadores 
* del : eliminara un par de clave valor
'''