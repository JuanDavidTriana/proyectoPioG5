def busqueda_lineal(objeto,lista):
    for i in range(len(lista)):
        if lista[i] == objeto:
            return i #Devuelve el indice del elemento

#Ejemplo de uso
numeros = [10, 20 ,30,45,90,11,22]

resultado = busqueda_lineal(45,numeros)

if resultado:
    print("Elemento encontrado")
    
else:
    print("Elemento no encontrado")